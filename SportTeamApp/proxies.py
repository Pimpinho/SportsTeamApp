# proxies.py

from .models import Inventory

class InventoryProxy:
    def __init__(self, inventory_id):
        self.inventory_id = inventory_id
        self._inventory = None
        self._cache = {}

    def _load_inventory(self):
        """Carrega o item do inventário do banco de dados se não estiver carregado."""
        if self._inventory is None:
            self._inventory = Inventory.objects.get(id=self.inventory_id)
        return self._inventory

    def get_product(self):
        if "product" not in self._cache:
            self._cache["product"] = self._load_inventory().product
        return self._cache["product"]

    def get_description(self):
        if "description" not in self._cache:
            self._cache["description"] = self._load_inventory().description
        return self._cache["description"]

    def get_quantity(self):
        if "quantity" not in self._cache:
            self._cache["quantity"] = self._load_inventory().quantity
        return self._cache["quantity"]

    def get_price(self):
        if "price" not in self._cache:
            self._cache["price"] = self._load_inventory().price
        return self._cache["price"]

    # Exemplo de um método que calcula o valor total do estoque do produto
    def get_total_value(self):
        if "total_value" not in self._cache:
            self._cache["total_value"] = self.get_quantity() * self.get_price()
        return self._cache["total_value"]
