from __future__ import annotations

from ipaddress import ip_address
from pathlib import Path

from .cache import Cache
from .config import DEFAULT_SOURCE_URL
from .downloader import Downloader
from .index import PrefixIndex
from .models import LookupResult, Match
from .updater import DatabaseUpdater


class NetworkClassifier:
    def __init__(
        self,
        database: str | Path | None = None,
        *,
        auto_update: bool = False,
        source_url: str = DEFAULT_SOURCE_URL,
        cache_dir: str | Path | None = None,
    ):

        self.index = PrefixIndex()

        self.cache = Cache(cache_dir)

        #
        # Використовуємо локальну базу
        #
        if database is not None:

            self.database = Path(database)

            self.index.load(
                self.database / "index.json"
            )

            return

        #
        # Використовуємо кеш
        #
        self.database = self.cache.path

        if auto_update:

            updater = DatabaseUpdater(
                downloader=Downloader(source_url),
                cache=self.cache,
            )

            updater.update_if_needed()

        self.index.load(
            self.cache.index_file
        )

    def lookup(
        self,
        ip: str,
    ) -> LookupResult:

        address = ip_address(ip)

        result = LookupResult(
            ip=ip,
        )

        for network, items in self.index.lookup(address):

            for item in items:

                result.matches.append(

                    Match(
                        network=str(network),
                        provider=item["provider"],
                        category=item["category"],
                    )

                )

        return result