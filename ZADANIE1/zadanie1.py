"""
Zadanie 1 - liczby Fibonacciego czterema sposobami: iteracyjnie, macierzowo
(szybkie potegowanie macierzy 2x2), biblioteka gmpy2 oraz wzorem Bineta
na liczbach zmiennoprzecinkowych (float).
"""

import math
import sys
import time

import gmpy2

# bardzo dlugie liczby: wylaczamy limit cyfr przy zamianie int -> str
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

N_POMIARY = [10_000, 100_000, 1_000_000]
PLIK_WYNIKU = "fib_1000000.txt"


def fib_iteracyjnie(n):
    """F(n) liczone petla: F(0) = 0, F(1) = 1, F(k) = F(k-1) + F(k-2)."""
    pass


def mnoz_macierze(a, b):
    """
    Iloczyn macierzy 2x2 zapisanych jako krotki (a11, a12, a21, a22).
    Przyklad: mnoz_macierze((1, 2, 3, 4), (5, 6, 7, 8)) -> (19, 22, 43, 50)
    """
    pass


def potega_macierzy(m, n):
    """
    M**n metoda szybkiego potegowania: zaczynamy od R = (1, 0, 0, 1) (macierz jednostkowa)
    i w petli po bitach n: jesli najmlodszy bit to 1, to R = R * M; potem M = M * M i n >>= 1.
    Do mnozenia uzywamy funkcji mnoz_macierze().
    """
    pass


def fib_macierzowo(n):
    """F(n) jako element b macierzy A**n, gdzie A = (1, 1, 1, 0)."""
    pass


def fib_gmpy2(n):
    """F(n) z gmpy2.fib(n), zamienione na int."""
    pass


def fib_binet(n):
    """F(n) ze wzoru Bineta na liczbach float: round(phi**n / sqrt(5)), phi = (1 + sqrt(5)) / 2."""
    pass


def pierwszy_blad_bineta():
    """Najmniejsze n, dla ktorego fib_binet(n) rozni sie od fib_iteracyjnie(n)."""
    pass


def main():
    # TODO: dla kazdego n z listy N_POMIARY zmierzyc czas trzech metod (time.perf_counter())
    #       i wypisac wiersz tabeli (n, liczba cyfr F(n), trzy czasy), np.
    #             n     cyfr   iteracyjnie    macierzowo         gmpy2
    #         10000     2090      0.0031 s      0.0003 s      0.0001 s
    # TODO: sprawdzic, czy wszystkie metody daja ten sam wynik, i wypisac
    #       "Wyniki wszystkich metod są zgodne."
    # TODO: F(n) dla ostatniego n z listy zapisac do pliku PLIK_WYNIKU (sama liczba)
    # TODO: wypisac "Wzór Bineta (float) myli się po raz pierwszy dla n = ..."
    pass


if __name__ == "__main__":
    main()
