from dataclasses import dataclass, field
from .match import Match


@dataclass(slots=True)
class LookupResult:

    ip: str
    matches: list[Match] = field(default_factory=list)

    def __bool__(self):
        return bool(self.matches)

    def __len__(self):
        return len(self.matches)

    @property
    def found(self): return bool(self.matches)

    @property
    def providers(self): return { m.provider for m in self.matches }

    @property
    def categories(self): return { m.category for m in self.matches }

    @property
    def networks(self): return { m.network for m in self.matches }

    @property
    def first(self): return self.matches[0] if self.matches else None

    def has_category( self, category: str, ): return category in self.categories