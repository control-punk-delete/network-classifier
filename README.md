# network-classifier

Бібліотека для класифікації IP-адрес та категорією
(cloud, cdn, hosting) на основі бази префіксів у форматі pytricia.

## Встановлення

```bash
pip install git+https://github.com/control-punk-delete/network-classifier.git          
```

## Використання з автооновленням із віддаленого джерела

```python
from network_classifier import NetworkClassifier

classifier = NetworkClassifier(auto_update=True)  # тягне дані за DEFAULT_SOURCE_URL
result = classifier.lookup("3.5.140.1")

# LookupResult(ip='3.5.140.1', matches=[Match(network='3.5.140.0/24', provider='Amazon AWS', category='cloud')])

```

За замовчуванням дані завантажуються з
`https://raw.githubusercontent.com/control-punk-delete/network-lookups/refs/heads/main/lookups/`
і кешуються в `~/.cache/network-classifier`. Повторні запуски не перезавантажують
базу, якщо версія (поле `generated` у `metadata.json`) не змінилась.

Для власного джерела:

```python
classifier = NetworkClassifier(auto_update=True, source_url="http://localhost:8000")
```

(джерело має віддавати `metadata.json` та `index.json` тими ж шляхами).