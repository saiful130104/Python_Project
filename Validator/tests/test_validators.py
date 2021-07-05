import pytest

from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert "Visa" == get_issuer("4343 4121 3343 2321")


def test_get_issuer_master_card():
    assert "MasterCard" == get_issuer("5343 4121 3343 2321")
    with pytest.raises(ValueError):
        get_issuer("5643 4121 3343 2321")
    with pytest.raises(ValueError):
        get_issuer("5643 4121 3343 232")


def test_get_issuer_american_express():
    assert "American Express" == get_issuer("3743 4121 3343 232")
    with pytest.raises(ValueError):
        get_issuer("3543 4121 3343 232")
    with pytest.raises(ValueError):
        get_issuer("3543 4121 3343 2342")


def test_length():
    assert "Visa" == get_issuer("4943 4121 3343 2321")
    with pytest.raises(ValueError):
        get_issuer("9943 4121 3343 2321")
    with pytest.raises(ValueError):
        get_issuer("9943 4121 3343 232")
