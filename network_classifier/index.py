import pytricia
import json

from __future__ import annotations

from ipaddress import ip_address
from ipaddress import ip_network
from pathlib import Path


class PrefixIndex:

    def __init__(self):

        self.ipv4 = pytricia.PyTricia(32)
        self.ipv6 = pytricia.PyTricia(128)


    def load(self, path: str | Path) -> None:

        path = Path(path)

        with path.open(encoding="utf8") as fp:
            entries = json.load(fp)

        for entry in entries:
            self.add( cidr=entry["cidr"], provider=entry["provider"], category=entry["category"] )



    def add(self,cidr: str, provider: str, category: str) -> None:

        network = ip_network(cidr)

        trie = ( self.ipv4 if network.version == 4 else self.ipv6 )

        key = str(network)

        if key not in trie:
            trie[key] = { "network": network, "matches": [] }

        trie[key]["matches"].append({ "provider": provider, "category": category })


    def lookup( self, ip ):

        if isinstance(ip, str):
            ip = ip_address(ip)

        trie = ( self.ipv4 if ip.version == 4 else self.ipv6 )

        try:
            result = trie[str(ip)]

        except KeyError:
            return []

        return [ (result["network"], result["matches"]) ]