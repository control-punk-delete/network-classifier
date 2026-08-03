# network-classifier

Бібліотека для класифікації IP-адрес та категорією
(cloud, cdn, hosting) на основі бази префіксів у форматі pytricia.

## Встановлення

Рекомендований варіант — встановлення в ізольоване віртуальне середовище:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
```

Також можна встановити прямо з GitHub:

```bash
python -m pip install "git+https://github.com/control-punk-delete/network-classifier.git"
```

Якщо під час встановлення виникає помилка на кшталт `Permission denied` для шляху в `/opt/.../venv`, це означає, що віртуальне середовище належить іншому користувачу або системному процесу. У такому випадку використайте власне середовище або встановлення в користувацький простір:

```bash
python -m pip install --user .
```

Видалення пакету:

```bash
python -m pip uninstall network-classifier
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