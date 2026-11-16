import re

import pytest

import ZADANIE1.zadanie1 as z1


def fib_wzorcowy(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def test_fib_iteracyjnie_poczatek():
    assert [z1.fib_iteracyjnie(n) for n in range(12)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fib_iteracyjnie_100():
    assert z1.fib_iteracyjnie(100) == 354224848179261915075


def test_mnoz_macierze():
    assert z1.mnoz_macierze((1, 2, 3, 4), (5, 6, 7, 8)) == (19, 22, 43, 50)
    assert z1.mnoz_macierze((1, 0, 0, 1), (2, 3, 4, 5)) == (2, 3, 4, 5)


@pytest.mark.parametrize("n, oczekiwane", [(0, (1, 0, 0, 1)), (1, (1, 1, 1, 0)), (5, (8, 5, 5, 3)),
                                           (6, (13, 8, 8, 5))])
def test_potega_macierzy(n, oczekiwane):
    assert z1.potega_macierzy((1, 1, 1, 0), n) == oczekiwane


def test_potega_macierzy_jest_szybka(monkeypatch):
    licznik = [0]
    oryginal = z1.mnoz_macierze

    def liczace(a, b):
        licznik[0] += 1
        return oryginal(a, b)

    monkeypatch.setattr(z1, "mnoz_macierze", liczace)
    assert z1.potega_macierzy((1, 1, 1, 0), 1000)[1] == fib_wzorcowy(1000)
    assert licznik[0] <= 22, "Szybkie potegowanie: okolo 2 * log2(n) mnozen, a nie n"


def test_fib_macierzowo_zgodne_z_definicja():
    for n in range(300):
        assert z1.fib_macierzowo(n) == fib_wzorcowy(n), f"n = {n}"


def test_fib_macierzowo_duze_n():
    assert z1.fib_macierzowo(10_000) == fib_wzorcowy(10_000)


def test_fib_gmpy2():
    wynik = z1.fib_gmpy2(1000)
    assert type(wynik) is int
    assert wynik == fib_wzorcowy(1000)


def test_fib_binet_dla_malych_n():
    for n in range(60):
        wynik = z1.fib_binet(n)
        assert type(wynik) is int
        assert wynik == fib_wzorcowy(n), f"n = {n}"


def test_pierwszy_blad_bineta():
    assert z1.pierwszy_blad_bineta() == 71


def test_main(monkeypatch, tmp_path, capsys):
    plik = tmp_path / "wynik.txt"
    monkeypatch.setattr(z1, "N_POMIARY", [10, 1000])
    monkeypatch.setattr(z1, "PLIK_WYNIKU", str(plik))
    z1.main()
    out = capsys.readouterr().out
    wiersze = re.findall(r"^\s*(\d+)\s+(\d+)\s+[\d.]+ s\s+[\d.]+ s\s+[\d.]+ s\s*$", out, re.MULTILINE)
    assert [(int(n), int(c)) for n, c in wiersze] == [(10, 2), (1000, 209)], "Wiersz tabeli dla kazdego n"
    assert "Wyniki wszystkich metod są zgodne." in out
    assert re.search(r"Bineta.*71", out)
    assert plik.read_text(encoding="utf-8").strip() == str(fib_wzorcowy(1000))
