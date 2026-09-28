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


def test_transfer_moves_stock():
    ledger = Ledger()
    ledger.add("a", 5)
    ledger.transfer("a", "b", 2)
    assert (ledger.count("a"), ledger.count("b")) == (3, 2)
