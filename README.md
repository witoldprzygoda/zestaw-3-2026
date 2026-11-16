# Zestaw 3 - Język Python

Trzy zadania laboratoryjne. Pełna treść zadań znajduje się w dokumencie PDF zestawu.

## Zawartość repozytorium

| Katalog    | Plik do uzupełnienia | Testy                    | Punkty |
|------------|----------------------|--------------------------|--------|
| `ZADANIE1` | `zadanie1.py`        | `tests/test_zadanie1.py` | 1      |
| `ZADANIE2` | `zadanie2.py`        | `tests/test_zadanie2.py` | 2      |
| `ZADANIE3` | `zadanie3.py`        | `tests/test_zadanie3.py` | 2      |

W katalogu `ZADANIE2` są też dane `linie_tramwajowe.json` oraz skrypt `pobierz_dane.py`,
który pobiera aktualny rozkład tramwajów ZTP Kraków (GTFS) i zapisuje te dane na nowo.

## Przygotowanie

```
python -m pip install -r requirements.txt
```

## Uruchamianie testów

```
python -m pytest            # wszystkie zadania
python -m pytest ZADANIE1   # jedno zadanie
python -m pytest -v         # z listą poszczególnych testów
```

Testy nie korzystają z sieci. Nie zmieniaj plików z testami ani nazw funkcji w kodzie początkowym.
