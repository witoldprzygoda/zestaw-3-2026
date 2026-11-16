"""
Pobiera aktualny rozklad tramwajow ZTP Krakow (format GTFS) i zapisuje
plik linie_tramwajowe.json, uzywany w zadaniu 2.

Uruchomienie (z glownego katalogu repozytorium):
    python ZADANIE2/pobierz_dane.py

GTFS to plik ZIP z tabelami CSV (routes, trips, stop_times, stops, shapes).
Dla kazdej linii bierzemy kierunek 0 i najczestszy w rozkladzie przebieg kursu:
kolejne przystanki (nazwa i wspolrzedne) oraz trase po torach (shapes).
"""

import collections
import csv
import io
import json
import os
import urllib.request
import zipfile

URL = "https://gtfs.ztp.krakow.pl/GTFS_KRK_T.zip"
PLIK_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linie_tramwajowe.json")


def tabela(archiwum, nazwa):
    """Wiersze pliku CSV z archiwum ZIP jako lista slownikow."""
    with archiwum.open(nazwa) as f:
        return list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8-sig")))


def przetworz(dane_zip):
    with zipfile.ZipFile(io.BytesIO(dane_zip)) as z:
        linie = {r["route_id"]: r["route_short_name"] for r in tabela(z, "routes.txt")}
        przystanki = {s["stop_id"]: s for s in tabela(z, "stops.txt")}
        kursy = tabela(z, "trips.txt")
        wersja = tabela(z, "feed_info.txt")[0].get("feed_version", "")
        kolejnosc = collections.defaultdict(list)
        for st in tabela(z, "stop_times.txt"):
            kolejnosc[st["trip_id"]].append((int(st["stop_sequence"]), st["stop_id"]))
        punkty = collections.defaultdict(list)
        for p in tabela(z, "shapes.txt"):
            punkty[p["shape_id"]].append((int(p["shape_pt_sequence"]), float(p["shape_pt_lat"]),
                                          float(p["shape_pt_lon"])))

    # przebiegi kursow: (linia, kierunek) -> licznik sekwencji przystankow
    przebiegi = collections.defaultdict(collections.Counter)
    ksztalt = {}
    for k in kursy:
        sekwencja = tuple(sid for _, sid in sorted(kolejnosc[k["trip_id"]]))
        przebiegi[(k["route_id"], k["direction_id"])][sekwencja] += 1
        ksztalt[(k["route_id"], sekwencja)] = k["shape_id"]

    wynik = []
    for route_id, numer in linie.items():
        licznik = przebiegi.get((route_id, "0")) or przebiegi.get((route_id, "1"))
        if not licznik:
            continue
        sekwencja = licznik.most_common(1)[0][0]
        wynik.append({
            "linia": numer,
            "przystanki": [{"nazwa": przystanki[s]["stop_name"],
                            "lat": round(float(przystanki[s]["stop_lat"]), 5),
                            "lon": round(float(przystanki[s]["stop_lon"]), 5)} for s in sekwencja],
            "trasa": [[round(lat, 5), round(lon, 5)] for _, lat, lon in sorted(punkty[ksztalt[(route_id, sekwencja)]])],
        })
    wynik.sort(key=lambda l: int(l["linia"]) if l["linia"].isdigit() else 10 ** 6)
    return {"opis": "Linie tramwajowe w Krakowie: przystanki i trasy (dane GTFS ZTP Kraków)",
            "zrodlo": URL, "wersja_danych": wersja, "liczba_linii": len(wynik), "linie": wynik}


def main():
    print("Pobieranie", URL)
    with urllib.request.urlopen(URL, timeout=60) as odp:
        dane_zip = odp.read()
    dane = przetworz(dane_zip)
    with open(PLIK_JSON, "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, separators=(",", ":"))
    print(f"Zapisano {os.path.basename(PLIK_JSON)}: {dane['liczba_linii']} linii, "
          f"wersja danych {dane['wersja_danych']}")


if __name__ == "__main__":
    main()
