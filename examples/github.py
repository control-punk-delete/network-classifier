from network_classifier import NetworkClassifier


classifier = NetworkClassifier(
    auto_update=True,
)


test_ips = [
    "1.1.1.1",
    "8.8.8.8",
    "52.95.110.1",
]


for ip in test_ips:

    result = classifier.lookup(ip)

    print(result)

