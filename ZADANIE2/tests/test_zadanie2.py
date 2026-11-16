import os
import re

import pytest

import ZADANIE2.zadanie2 as z2

PLIK_TESTOWY = os.path.join(os.path.dirname(__file__), "dane_testowe.json")


@pytest.fixture
def dane():
    return z2.wczytaj(PLIK_TESTOWY)


def test_wczytaj(dane):
    assert [l["linia"] for l in dane["linie"]] == ["2", "10", "3"]


def test_liczba_przystankow(dane):
    assert z2.liczba_przystankow(dane) == {"2": 3, "10": 2, "3": 3}


def test_unikalne_przystanki(dane):
    assert z2.unikalne_przystanki(dane) == 4


def test_linie_przez_przystanek(dane):
    assert z2.linie_przez_przystanek(dane) == {
        "Alfa": ["2", "3"], "Beta": ["2", "3", "10"], "Gamma": ["2"], "Delta": ["3", "10"]}


def test_najwazniejsze_przystanki(dane):
    assert z2.najwazniejsze_przystanki(dane, ile=3) == [("Beta", 3), ("Alfa", 2), ("Delta", 2)]
    assert z2.najwazniejsze_przystanki(dane, ile=1) == [("Beta", 3)]
    assert len(z2.najwazniejsze_przystanki(dane)) == 4


def test_odleglosc_km():
    assert z2.odleglosc_km((0.0, 0.0), (0.0, 1.0)) == pytest.approx(111.195, abs=1e-3)
    assert z2.odleglosc_km((50.0, 20.0), (50.0, 20.01)) == pytest.approx(0.7147, abs=1e-3)
    assert z2.odleglosc_km((50.06, 19.94), (50.06, 19.94)) == 0.0


def test_dlugosc_trasy_km():
    assert z2.dlugosc_trasy_km([[0.0, 0.0], [0.0, 1.0], [0.0, 2.0]]) == pytest.approx(222.39, abs=1e-2)
    assert z2.dlugosc_trasy_km([[50.0, 20.0]]) == 0
    assert z2.dlugosc_trasy_km([]) == 0


def test_rysuj_mape(dane, tmp_path):
    plik = tmp_path / "mapa.html"
    z2.rysuj_mape(dane, str(plik))
    html = plik.read_text(encoding="utf-8")
    assert html.count("L.polyline(") == 3, "Jedna trasa (PolyLine) na linie"
    assert html.count("L.circleMarker(") == 4, "Kazdy przystanek raz (CircleMarker)"
    assert "L.control.layers" in html, "Przelacznik warstw (LayerControl)"
    assert "Linia 10: Beta - Delta" in html
    assert "Beta: linie 2, 3, 10" in html


def test_main(tmp_path, capsys):
    plik = tmp_path / "mapa.html"
    z2.main(PLIK_TESTOWY, str(plik))
    out = capsys.readouterr().out
    wiersze = re.findall(r"^\s*(\d+)\s+(\d+)\s+([\d.]+) km", out, re.MULTILINE)
    assert [(n, int(p)) for n, p, _ in wiersze] == [("2", 3), ("3", 3), ("10", 2)]
    assert [float(km) for _, _, km in wiersze] == pytest.approx([1.8, 1.8, 1.1], abs=0.05)
    assert "Różnych przystanków: 4" in out
    assert plik.exists()


def test_dane_w_repozytorium():
    dane = z2.wczytaj(z2.PLIK_DANYCH)
    assert len(dane["linie"]) >= 10
    for linia in dane["linie"]:
        assert {"linia", "przystanki", "trasa"} <= set(linia)
        assert len(linia["przystanki"]) >= 2 and len(linia["trasa"]) >= 2
