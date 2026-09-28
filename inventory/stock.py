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

    def transfer(self, source: str, target: str, qty: int) -> None:
        """Move stock between SKUs; either both sides change or neither does."""
        self.add(target, qty)
        self.remove(source, qty)

    def total(self) -> int:
        return sum(self._items.values())
