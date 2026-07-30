from network_classifier import NetworkClassifier



classifier = NetworkClassifier(
    auto_update=True,
    source_url=(
        "http://localhost:8000"
    ),
)



result = classifier.lookup(
    "1.1.1.1"
)



print(
    result.providers
)


print(
    result.categories
)