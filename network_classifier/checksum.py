import hashlib

from pathlib import Path
from __future__ import annotations


def sha256_file(path: Path) -> str:
    sha256 = hashlib.sha256()

    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(65536),b""):
            sha256.update(chunk)

    return sha256.hexdigest()