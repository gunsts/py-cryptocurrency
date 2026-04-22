import pytest
from app import main


def test_exchange_rate_prediction_increase(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock exchange rate prediction increase more than 5%
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.1)
    assert main.cryptocurrency_action(1.0) == "Buy more cryptocurrency"


def test_exchange_rate_prediction_decrease(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock exchange rate prediction decrease more than 5%
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 0.8)
    assert main.cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


def test_exchange_rate_prediction_in_boundary(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock exchange rate prediction within -0.5% and 0.5% boundary
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.01)
    assert main.cryptocurrency_action(1.0) == "Do nothing"
