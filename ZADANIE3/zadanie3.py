"""
Zadanie 3 - notowania bitcoina: pobieranie danych (yfinance), srednie kroczace
50- i 200-dniowe, ich przeciecia (zloty krzyz i krzyz smierci) oraz najwiekszy
dzienny obrot liczony w BTC.
"""

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

SYMBOL = "BTC-USD"
POCZATEK = "2024-01-01"
PLIK_CSV = "btc_usd.csv"
PLIK_WYKRESU = "btc_srednie.png"


def pobierz(symbol=SYMBOL, start=POCZATEK, koniec=None):
    """
    Notowania dzienne z yf.download(); kolumny jednopoziomowe (multi_level_index=False):
    Close, High, Low, Open, Volume, indeks: daty. koniec=None oznacza "do dzis".
    Gdy nic nie pobrano (pusta tabela), zglaszamy wyjatek RuntimeError.
    """
    pass


def wczytaj_csv(plik):
    """Wczytuje notowania zapisane metoda to_csv(); indeks: kolumna Date jako daty (parse_dates)."""
    pass


def srednie_kroczace(dane):
    """Nowa tabela: kopia danych z dodanymi kolumnami MA50 i MA200 (srednie kroczace ceny Close)."""
    pass


def przeciecia(dane):
    """
    Dni przeciecia srednich: lista krotek (data "RRRR-MM-DD", rodzaj), gdzie rodzaj to
    "złoty krzyż" (roznica MA50 - MA200 zmienia sie z ujemnej na dodatnia)
    albo "krzyż śmierci" (z dodatniej na ujemna). Pomijamy dni bez obu srednich.
    """
    pass


def max_dzienny_obrot_btc(dane):
    """Dzien z najwiekszym obrotem w BTC (Volume / Close): krotka (data "RRRR-MM-DD", liczba BTC jako int)."""
    pass


def rysuj(dane, punkty, plik_png):
    """
    Wykres ceny zamkniecia i obu srednich z zaznaczonymi przecieciami (punkty z funkcji przeciecia);
    zapis do pliku plik_png, bez plt.show().
    """
    pass


def main():
    # TODO: pobrac notowania (pobierz) i zapisac je do pliku PLIK_CSV
    # TODO: dodac srednie kroczace, wypisac zakres dat i liczbe dni notowan
    # TODO: wypisac przeciecia srednich, kazde w osobnym wierszu, np.
    #         2024-10-28  złoty krzyż
    # TODO: wypisac "Największy dzienny obrót: ... BTC (RRRR-MM-DD)"
    # TODO: narysowac wykres do pliku PLIK_WYKRESU
    pass


if __name__ == "__main__":
    main()
