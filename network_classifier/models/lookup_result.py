from dataclasses import dataclass, field

from .match import Match


@dataclass(slots=True)
class LookupResult:

    ip: str

    matches: list[Match] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.matches)

    @property
    def found(self) -> bool:
        return bool(self.matches)

    @property
    def providers(self) -> set[str]:
        return {
            match.provider
            for match in self.matches
        }

    @property
    def categories(self) -> set[str]:
        return {
            match.category
            for match in self.matches
        }

    @property
    def networks(self) -> set[str]:
        return {
            match.network
            for match in self.matches
        }

    @property
    def first(self) -> Match | None:
        if not self.matches:
            return None

        return self.matches[0]

    def has_category(
        self,
        category: str,
    ) -> bool:

        return category in self.categories

    def has_provider(
        self,
        provider: str,
    ) -> bool:

        return provider in self.providers

    @property
    def is_cloud(self) -> bool:
        return self.has_category("cloud")

    @property
    def is_cdn(self) -> bool:
        return self.has_category("cdn")

    @property
    def is_hosting(self) -> bool:
        return self.has_category("hosting")

    @property
    def is_vpn(self) -> bool:
        return self.has_category("vpn")

    @property
    def is_proxy(self) -> bool:
        return self.has_category("proxy")

    @property
    def is_tor(self) -> bool:
        return self.has_category("tor")

    @property
    def is_anycast(self) -> bool:
        return self.has_category("anycast")

    @property
    def is_scanner(self) -> bool:
        return self.has_category("scanner")