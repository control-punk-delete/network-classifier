from pathlib import Path

from network_classifier import NetworkClassifier


ROOT = Path(__file__).resolve().parent.parent


print("ROOT:", ROOT)


classifier = NetworkClassifier(
    ROOT / "test-data"
)


print(
    "Loaded metadata:",
    classifier.metadata
)


result = classifier.lookup(
    "1.1.1.1"
)


print(
    "Hits:",
    len(result)
)


print(
    "Providers:",
    result.providers
)