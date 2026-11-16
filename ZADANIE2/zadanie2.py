"""
Zadanie 2 - siec tramwajowa Krakowa: statystyki linii i przystankow,
dlugosc tras ze wzoru haversine oraz interaktywna mapa (folium).

Dane: plik linie_tramwajowe.json (rozklad ZTP Krakow w formacie GTFS,
przetworzony skryptem pobierz_dane.py).
"""

import json
import math
import os

import folium

PLIK_DANYCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linie_tramwajowe.json")
PLIK_MAPY = "mapa_tramwaje.html"
PROMIEN_ZIEMI_KM = 6371.0
KOLORY = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#a65628", "#f781bf",
          "#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02"]


def wczytaj(plik):
    """Wczytuje plik JSON z danymi linii (kodowanie utf-8) i zwraca slownik."""
    pass


def liczba_przystankow(dane):
    """Slownik {numer_linii: liczba_przystankow}, np. {"1": 28, "3": 24, ...}."""
    pass


def unikalne_przystanki(dane):
    """Liczba roznych nazw przystankow we wszystkich liniach."""
    pass


def linie_przez_przystanek(dane):
    """
    Slownik {nazwa_przystanku: lista numerow linii}; numery bez powtorzen,
    uporzadkowane rosnaco jak liczby: ["2", "3", "10"], a nie ["10", "2", "3"].
    """
    pass


def najwazniejsze_przystanki(dane, ile=5):
    """
    Lista krotek (nazwa, liczba_linii) dla przystankow z najwieksza liczba linii.
    Kolejnosc: malejaco wg liczby linii, przy rownej liczbie alfabetycznie.
    """
    pass


def odleglosc_km(p1, p2):
    """Odleglosc w km miedzy punktami (lat, lon) na kuli o promieniu PROMIEN_ZIEMI_KM (wzor haversine)."""
    pass


def dlugosc_trasy_km(trasa):
    """Suma odleglosci miedzy kolejnymi punktami trasy [[lat, lon], ...]; dla 0 lub 1 punktu: 0."""
    pass


def rysuj_mape(dane, plik_html):
    """
    Mapa folium (podklad "Esri.WorldGrayCanvas"):
    - kazda linia jako osobna warstwa folium.FeatureGroup(name="linia X") z trasa (folium.PolyLine),
      kolor z listy KOLORY, podpowiedz (tooltip) "Linia X: pierwszy przystanek - ostatni przystanek",
    - kazdy przystanek (raz, bez powtorzen) jako folium.CircleMarker w warstwie "przystanki",
      podpowiedz "Nazwa: linie 3, 9, 50",
    - przelacznik warstw folium.LayerControl().
    Zapisuje mape do pliku plik_html i zwraca obiekt mapy.
    """
    pass


def main(plik=PLIK_DANYCH, plik_html=PLIK_MAPY):
    # TODO: wczytac dane i wypisac tabele linii, malejaco wg liczby przystankow
    #       (przy rownej liczbie rosnaco wg numeru linii), np.
    #       linia  przystanki    długość  trasa
    #          74          41    22.2 km  Wzgórza Krzesławickie - Kurdwanów P+R
    # TODO: wypisac "Różnych przystanków: ..." oraz piec najwazniejszych przystankow
    # TODO: narysowac mape i wypisac "Mapę zapisano w pliku ..."
    pass


if __name__ == "__main__":
    main()
