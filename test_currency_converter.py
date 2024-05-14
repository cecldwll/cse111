import pytest
from currency_converter import get_exchange_rates, convert_currency

def test_get_exchange_rates():
    """Test the get_exchange_rates function to ensure it returns a dictionary with rates."""
    rates = get_exchange_rates()
    assert isinstance(rates, dict) and "USD" in rates, "The function should return a dictionary containing 'USD'."

def test_convert_currency_identical_currencies():
    """Test currency conversion when from and to currencies are the same."""
    exchange_rates = {"USD": 1, "EUR": 0.9}
    amount = convert_currency("USD", "USD", 100, exchange_rates)
    assert amount == 100, "Conversion with identical currencies should return the original amount."

def test_convert_currency_unsupported_currency():
    """Test currency conversion with an unsupported currency."""
    exchange_rates = {"USD": 1, "EUR": 0.9}
    amount = convert_currency("USD", "ABC", 100, exchange_rates)
    assert amount is None, "Conversion with an unsupported currency should return None."

def test_convert_currency():
    """Test currency conversion with supported currencies."""
    exchange_rates = {"USD": 1, "EUR": 0.9, "JPY": 110}
    # USD to EUR
    amount = convert_currency("USD", "EUR", 100, exchange_rates)
    assert amount == 90, "100 USD should be 90 EUR."
    # EUR to JPY (via USD)
    amount = convert_currency("EUR", "JPY", 100, exchange_rates)
    assert pytest.approx(amount, 0.01) == 12222.22, "100 EUR should be approximately 12222.22 JPY."

