import requests

from __future__ import annotations
from pathlib import Path

class Downloader:

    def __init__( self, source_url: str ) -> None:
        self.source_url = ( source_url.rstrip("/") )


    def download(self, filename: str, destination: Path) -> None:
        url = (f"{self.source_url}/{filename}" )
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        destination.write_bytes(response.content)


    def fetch_text( self, filename: str ) -> str:

        url = ( f"{self.source_url}/{filename}" )
        response = requests.get( url, timeout=30)
        response.raise_for_status()
        return response.text