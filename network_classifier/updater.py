from __future__ import annotations

import json

from .checksum import sha256_file


class DatabaseUpdater:

    def __init__( self, downloader, cache) -> None:
        self.downloader = downloader
        self.cache = cache

    def update_if_needed(self) -> bool:

        remote_metadata = json.loads( self.downloader.fetch_text( "metadata.json" ))
        local_metadata = {}

        if self.cache.metadata_file.exists():
            local_metadata = ( self.cache.load_metadata() )

        if (self.cache.exists() and self._same_version(local_metadata,remote_metadata ) and self._verify()):
            return False

        self.downloader.download("index.json", self.cache.index_file)


        self.cache.metadata_file.write_text(json.dumps( remote_metadata, indent=2), encoding="utf8" )
        self._verify()

        return True


    def _same_version( self, local: dict, remote: dict ) -> bool:

        def version_key( metadata: dict ):
            return ( metadata.get("generated") or metadata.get("lookup_version") )

        return (version_key(local) ==version_key(remote))



    def _verify( self ) -> bool:

        metadata = ( self.cache.load_metadata() )
        expected = ( metadata.get("files",{}).get("index.json",{}).get("sha256"))

        if not expected:
            return True

        actual = sha256_file(self.cache.index_file )

        if expected != actual:
            raise RuntimeError("Database checksum mismatch")

        return True