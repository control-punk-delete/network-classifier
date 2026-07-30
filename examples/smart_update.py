from network_classifier import NetworkClassifier



classifier = NetworkClassifier(
    auto_update=True,
)



result = classifier.lookup(
    "1.1.1.1"
)


print(
    result
)