import os
import re

import matplotlib

matplotlib.use("Agg")

import pandas as pd  # noqa: E402
import pytest  # noqa: E402

import ZADANIE3.zadanie3 as z3  # noqa: E402

# notowania BTC-USD z yfinance: 2024-01-01 ... 2026-11-15 (stale dane do testow)
PLIK_TESTOWY = os.path.join(os.path.dirname(__file__), "btc_usd.csv")

PRZECIECIA = [("2024-08-10", "krzyż śmierci"), ("2024-10-28", "złoty krzyż"),
              ("2025-04-07", "krzyż śmierci"), ("2025-05-22", "złoty krzyż"),
              ("2025-11-16", "krzyż śmierci"), ("2026-09-08", "złoty krzyż")]


@pytest.fixture
def notowania():
    return pd.read_csv(PLIK_TESTOWY, index_col="Date", parse_dates=True)


def test_wczytaj_csv():
    dane = z3.wczytaj_csv(PLIK_TESTOWY)
    assert isinstance(dane.index, pd.DatetimeIndex)
    assert {"Close", "Volume"} <= set(dane.columns)
    assert len(dane) == 1050


def test_pobierz_kolumny_jednopoziomowe(monkeypatch, notowania):
    wywolania = []

    def falszywe_download(tickers, *args, **kwargs):
        wywolania.append((tickers, args, kwargs))
        dane = notowania.copy()
        if kwargs.get("multi_level_index", True):
            # tak jak yfinance: domyslnie kolumny dwupoziomowe (Price, Ticker)
            dane.columns = pd.MultiIndex.from_product([dane.columns, [tickers]], names=["Price", "Ticker"])
        return dane

    monkeypatch.setattr(z3.yf, "download", falszywe_download)
    dane = z3.pobierz("BTC-USD", "2024-01-01")
    assert wywolania and wywolania[0][0] == "BTC-USD"
    assert isinstance(dane["Close"], pd.Series), "Kolumny jednopoziomowe: dane['Close'] to jedna kolumna"
    assert len(dane) == len(notowania)


def test_pobierz_pusta_tabela(monkeypatch):
    monkeypatch.setattr(z3.yf, "download", lambda *a, **k: pd.DataFrame())
    with pytest.raises(RuntimeError):
        z3.pobierz("XYZ-USD", "2024-01-01")


def test_srednie_kroczace(notowania):
    wynik = z3.srednie_kroczace(notowania)
    assert "MA50" not in notowania.columns, "Funkcja zwraca nowa tabele, nie zmienia danych wejsciowych"
    assert wynik["MA50"].isna().sum() == 49
    assert wynik["MA200"].isna().sum() == 199
    assert wynik["MA50"].iloc[49] == pytest.approx(notowania["Close"].iloc[:50].mean())
    assert wynik["MA200"].iloc[-1] == pytest.approx(notowania["Close"].iloc[-200:].mean())


def test_przeciecia_proste():
    dni = pd.date_range("2025-01-01", periods=6, freq="D")
    dane = pd.DataFrame({"MA50": [None, 1.0, 2.0, 3.0, 2.0, 1.0],
                         "MA200": [None, 2.0, 2.5, 2.5, 2.5, 2.5]}, index=dni)
    assert z3.przeciecia(dane) == [("2025-01-04", "złoty krzyż"), ("2025-01-05", "krzyż śmierci")]


def test_przeciecia_btc(notowania):
    assert z3.przeciecia(z3.srednie_kroczace(notowania)) == PRZECIECIA


def test_max_dzienny_obrot_btc(notowania):
    data, btc = z3.max_dzienny_obrot_btc(notowania)
    assert (data, btc) == ("2024-08-05", 2018672)
    assert type(btc) is int


def test_main(monkeypatch, tmp_path, capsys, notowania):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(z3, "pobierz", lambda *a, **k: notowania.copy())
    z3.main()
    out = capsys.readouterr().out
    assert re.findall(r"(\d{4}-\d{2}-\d{2})\s+(złoty krzyż|krzyż śmierci)", out) == PRZECIECIA
    assert re.search(r"Największy dzienny obrót: 2018672 BTC \(2024-08-05\)", out)
    assert (tmp_path / z3.PLIK_CSV).exists()
    assert (tmp_path / z3.PLIK_WYKRESU).stat().st_size > 10_000
