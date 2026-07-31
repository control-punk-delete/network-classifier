from dataclasses import dataclass, field

from .match import Match


@dataclass(slots=True)
class LookupResult:

    ip: str

    matches: list[Match] = field(default_factory=list)

    def __bool__(self):
        return bool(self.matches)

    @property
    def found(self):
        return bool(self.matches)

    @property
    def providers(self):
        return {
            m.provider
            for m in self.matches
        }

    @property
    def categories(self):
        return {
            m.category
            for m in self.matches
        }

    @property
    def networks(self):
        return {
            m.network
            for m in self.matches
        }

    @property
    def first(self):
        return self.matches[0] if self.matches else None

    def has_category(
        self,
        category: str,
    ):
        return category in self.categories

    @property
    def is_cloud(self):
        return self.has_category("cloud")

    @property
    def is_cdn(self):
        return self.has_category("cdn")

    @property
    def is_hosting(self):
        return self.has_category("hosting")

    @property
    def is_vpn(self):
        return self.has_category("vpn")

    @property
    def is_proxy(self):
        return self.has_category("proxy")

    @property
    def is_tor(self):
        return self.has_category("tor")

    @property
    def is_anycast(self):
        return self.has_category("anycast")

    @property
    def is_scanner(self):
        return self.has_category("scanner")