from __future__ import annotations


from ipaddress import ip_address
from ipaddress import ip_network


import pytricia



class PyTriciaIndex:


    def __init__(self):

        self.ipv4 = pytricia.PyTricia(32)

        self.ipv6 = pytricia.PyTricia(128)



    def add(
        self,
        cidr: str,
        provider: str,
        category: str,
    ) -> None:


        network = ip_network(cidr)


        trie = (
            self.ipv4
            if network.version == 4
            else self.ipv6
        )


        key = str(network)


        if key not in trie:

            trie[key] = {

                "network": network,

                "matches": [],

            }


        trie[key]["matches"].append(

            {
                "provider": provider,
                "category": category,
            }

        )



    def lookup(
        self,
        ip,
    ):


        if isinstance(ip, str):

            ip = ip_address(ip)


        trie = (
            self.ipv4
            if ip.version == 4
            else self.ipv6
        )


        try:

            result = trie[str(ip)]

        except KeyError:

            return []


        return [

            (
                result["network"],
                result["matches"],
            )

        ]