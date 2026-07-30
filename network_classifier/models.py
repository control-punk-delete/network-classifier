from __future__ import annotations

from dataclasses import dataclass, field
from ipaddress import IPv4Address
from ipaddress import IPv6Address
from ipaddress import IPv4Network
from ipaddress import IPv6Network


IPAddress = IPv4Address | IPv6Address
IPNetwork = IPv4Network | IPv6Network


@dataclass(slots=True, frozen=True)
class Match:

    provider: str

    category: str


@dataclass(slots=True, frozen=True)
class LookupHit:

    network: IPNetwork

    matches: list[Match]

    @property
    def cidr(self) -> str:

        return str(self.network)


@dataclass(slots=True)
class LookupResult:

    ip: IPAddress

    hits: list[LookupHit] = field(
        default_factory=list
    )


    def add(
        self,
        hit: LookupHit,
    ) -> None:

        self.hits.append(hit)


    @property
    def matches(self) -> list[Match]:

        return [
            match
            for hit in self.hits
            for match in hit.matches
        ]


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
    def is_cdn(self) -> bool:

        return "cdn" in self.categories


    @property
    def is_cloud(self) -> bool:

        return "cloud" in self.categories


    @property
    def has_matches(self) -> bool:

        return bool(self.hits)


    def __iter__(self):

        return iter(self.hits)


    def __len__(self):

        return len(self.hits)


    def __bool__(self):

        return self.has_matches