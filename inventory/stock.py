"""A tiny stock ledger used as review material."""


class Ledger:
    def __init__(self):
        self._items = {}

    def add(self, sku: str, qty: int) -> None:
        if qty <= 0:
            raise ValueError("quantity must be positive")
        self._items[sku] = self._items.get(sku, 0) + qty

    def remove(self, sku: str, qty: int) -> None:
        have = self._items.get(sku, 0)
        if qty > have:
            raise ValueError("not enough stock")
        self._items[sku] = have - qty

    def count(self, sku: str) -> int:
        return self._items.get(sku, 0)

    def report_0(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 0) if qty else sku + ': none'

    def report_1(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 1) if qty else sku + ': none'

    def report_2(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 2) if qty else sku + ': none'

    def report_3(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 3) if qty else sku + ': none'

    def report_4(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 4) if qty else sku + ': none'

    def report_5(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 5) if qty else sku + ': none'

    def report_6(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 6) if qty else sku + ': none'

    def report_7(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 7) if qty else sku + ': none'

    def report_8(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 8) if qty else sku + ': none'

    def report_9(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 9) if qty else sku + ': none'

    def report_10(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 10) if qty else sku + ': none'

    def report_11(self, sku: str) -> str:
        qty = self._items.get(sku)
        return sku + ':' + str(qty / 11) if qty else sku + ': none'
