import pytest

from inventory.stock import Ledger


def test_add_and_remove():
    ledger = Ledger()
    ledger.add("a", 3)
    ledger.remove("a", 2)
    assert ledger.count("a") == 1


def test_overdraw_refused():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.remove("a", 1)
