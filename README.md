# network-classifier

Бібліотека для класифікації IP-адрес за провайдером та категорією
(cloud, cdn, dns, hosting, vpn, proxy, tor, anycast, scanner тощо)
на основі бази префіксів у форматі pytricia.

## Встановлення

```bash
pip install -e .
```

## Використання з локальною базою

```python
from network_classifier import NetworkClassifier

classifier = NetworkClassifier("path/to/database")  # каталог з index.json (+ metadata.json)
result = classifier.lookup("1.1.1.1")

print(result.providers)   # {'Cloudflare'}
print(result.categories)  # {'dns'}
print(result.is_cdn)      # True/False
```

Формат `index.json`: список об'єктів `{"cidr": "...", "provider": "...", "category": "..."}`.
Приклад такої бази лежить у `test-data/` — див. `examples/simple.py`.

## Використання з автооновленням із віддаленого джерела

```python
from network_classifier import NetworkClassifier

classifier = NetworkClassifier(auto_update=True)  # тягне дані за DEFAULT_SOURCE_URL
result = classifier.lookup("52.95.110.1")
```

За замовчуванням дані завантажуються з
`https://raw.githubusercontent.com/control-punk-delete/cdn-lookup/refs/heads/main/output/`
і кешуються в `~/.cache/network-classifier`. Повторні запуски не перезавантажують
базу, якщо версія (поле `generated` у `metadata.json`) не змінилась.

Для власного джерела:

```python
classifier = NetworkClassifier(auto_update=True, source_url="http://localhost:8000")
```

(джерело має віддавати `metadata.json` та `index.json` тими ж шляхами).

## Приклади

- `examples/simple.py` — офлайн, на локальних тестових даних.
- `examples/github.py` — автооновлення з реального GitHub-джерела.
- `examples/smart_update.py` — демонстрація кешування/пропуску повторного завантаження.
- `examples/remote.py` — робота з власним self-hosted джерелом (потрібен сервер на `:8000`).

## CHANGELOG

### 0.2.0

- Виправлено `ImportError`: клас у `index.py` називався `PyTriciaIndex`,
  а `classifier.py` імпортував неіснуючий `PrefixIndex` — пакет узагалі
  не імпортувався.
- Додано метод `PrefixIndex.load()`, якого бракувало (класифікатор
  викликав його, але він ніде не був реалізований).
- Додано `NetworkClassifier.metadata` (використовувався в прикладах,
  але не існував).
- Додано `LookupResult.__len__` (використовувався в `examples/simple.py`).
- Виправлено звірку версій в `updater.py`: порівнювалось неіснуюче поле
  `"version"`, тоді як реальна схема метаданих використовує `"generated"`
  — через це кеш ніколи коректно не оновлювався б і ніколи б коректно
  не пропускав повторне завантаження.
- Додано відсутню залежність `requests` у `pyproject.toml`
  (використовується в `downloader.py`, але не була задекларована).
- Додано `test-data/` — робочий приклад локальної бази для офлайн-демо.
- Прибрано зайвий дублікат `__init__.py` у корені репозиторію.