from __future__ import annotations


import json

from ipaddress import ip_address
from pathlib import Path


from .cache import Cache
from .config import DEFAULT_SOURCE_URL
from .downloader import Downloader
from .index import PyTriciaIndex
from .updater import DatabaseUpdater


from .models import (
    LookupResult,
    LookupHit,
    Match,
)



class NetworkClassifier:


    def __init__(
        self,
        source: str | Path | None = None,
        cache: str | Path | None = None,
        auto_update: bool = False,
        source_url: str | None = None,
    ) -> None:


        self.index = PyTriciaIndex()


        self.metadata: dict = {}


        self.cache = Cache(
            cache
        )


        self.source_url = (
            source_url
            or DEFAULT_SOURCE_URL
        )



        #
        # Priority:
        #
        # 1. Explicit local source
        # 2. Remote update
        # 3. Existing cache
        #
        

        if source:


            self.load(
                source
            )


        elif auto_update:


            self.update_database()



        elif self.cache.exists():


            self.load_cache()



        else:


            raise RuntimeError(
                "Database unavailable"
            )



    def load(
        self,
        source: str | Path,
    ) -> None:


        source = Path(
            source
        )


        with (
            source / "metadata.json"
        ).open(
            encoding="utf8"
        ) as fp:


            self.metadata = json.load(
                fp
            )



        with (
            source / "index.json"
        ).open(
            encoding="utf8"
        ) as fp:


            rows = json.load(
                fp
            )



        self._build_index(
            rows
        )



    def load_cache(
        self,
    ) -> None:


        #
        # Important:
        # recreate index before rebuild
        #

        self.index = PyTriciaIndex()


        self.metadata = (
            self.cache.load_metadata()
        )


        rows = (
            self.cache.load_index()
        )


        self._build_index(
            rows
        )



    def _build_index(
        self,
        rows: list[dict],
    ) -> None:


        for row in rows:


            self.index.add(

                cidr=row["cidr"],

                provider=row["provider"],

                category=row["category"],

            )



    def update_database(
        self,
    ) -> None:


        downloader = Downloader(
            self.source_url
        )


        updater = DatabaseUpdater(

            downloader,

            self.cache,

        )


        updater.update_if_needed()



        self.load_cache()



    def lookup(
        self,
        ip: str,
    ):


        address = ip_address(
            ip
        )


        matches = (
            self.index.lookup(
                address
            )
        )


        result = []


        for network, items in matches:


            result.append(

                {
                    "network": str(network),

                    "matches": [

                        {
                            "provider": item["provider"],

                            "category": item["category"],

                        }

                        for item in items

                    ],

                }

            )


        return result