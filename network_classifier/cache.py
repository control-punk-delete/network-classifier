from __future__ import annotations


import json

from pathlib import Path
from typing import Any


from .config import DEFAULT_CACHE_DIR



class Cache:


    def __init__(
        self,
        path: str | Path | None = None,
    ) -> None:


        if path:

            self.path = Path(path)

        else:

            self.path = Path(
                DEFAULT_CACHE_DIR
            ).expanduser()



        self.path.mkdir(
            parents=True,
            exist_ok=True,
        )



    @property
    def metadata_file(self):

        return (
            self.path
            /
            "metadata.json"
        )


    @property
    def index_file(self):

        return (
            self.path
            /
            "index.json"
        )



    def exists(self) -> bool:

        return (

            self.metadata_file.exists()

            and

            self.index_file.exists()

        )



    def save(
        self,
        metadata: dict,
        index: list[dict],
    ) -> None:


        with self.metadata_file.open(
            "w",
            encoding="utf8",
        ) as fp:

            json.dump(
                metadata,
                fp,
                indent=2,
            )



        with self.index_file.open(
            "w",
            encoding="utf8",
        ) as fp:

            json.dump(
                index,
                fp,
                indent=2,
            )



    def load_metadata(
        self,
    ) -> dict[str, Any]:


        with self.metadata_file.open(
            encoding="utf8",
        ) as fp:

            return json.load(fp)



    def load_index(
        self,
    ) -> list[dict]:


        with self.index_file.open(
            encoding="utf8",
        ) as fp:

            return json.load(fp)

    @property
    def version_file(self):

        return (
            self.path
            /
            "metadata.json"
        )
        
    def get_metadata(self):

        if not self.metadata_file.exists():

            return {}

        return self.load_metadata()