from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Match:
    network: str
    provider: str
    category: str