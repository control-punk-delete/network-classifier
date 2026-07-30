from pathlib import Path

from network_classifier.cache import Cache


ROOT = Path(__file__).resolve().parent.parent


cache_path = ROOT / "cache-test"


cache = Cache(
    cache_path
)


metadata = {
    "schema": 1,
    "providers": 1,
    "prefixes": 1,
}


index = [
    {
        "cidr": "1.1.1.0/24",
        "provider": "Cloudflare",
        "category": "cdn",
    }
]


print(
    "Cache path:",
    cache.path
)


print(
    "Exists before:",
    cache.exists()
)


cache.save(
    metadata,
    index,
)


print(
    "Exists after save:",
    cache.exists()
)


loaded_metadata = cache.load_metadata()

loaded_index = cache.load_index()


print(
    "Metadata:",
    loaded_metadata
)


print(
    "Index:",
    loaded_index
)


assert loaded_metadata == metadata

assert loaded_index == index


print(
    "Cache test OK"
)