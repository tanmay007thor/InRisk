
class ProductService:
    def __init__(self):
        self.products = []
        self._fetch_initial_products()

    def _fetch_initial_products(self):
        import requests
        try:
            response = requests.get("https://dummyjson.com/products")
            response.raise_for_status()
            self.products = response.json().get("products", [])
        except Exception as e:
            print(f"Error fetching initial data: {e}")
            self.products = []

    def get_all_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)
