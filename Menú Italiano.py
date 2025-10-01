class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total(self, quantity: int = 1) -> float:
        return self.price * quantity

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:,.0f} COP"


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size

    def __str__(self) -> str:
        return f"{self.name} ({self.size}) - ${self.price:,.0f} COP"


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, portion: str):
        super().__init__(name, price)
        self.portion = portion

    def __str__(self) -> str:
        return f"{self.name} [{self.portion}] - ${self.price:,.0f} COP"


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, is_vegetarian: bool = False):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

    def __str__(self) -> str:
        veg = " (Vegetariano)" if self.is_vegetarian else ""
        return f"{self.name}{veg} - ${self.price:,.0f} COP"


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, sweet_level: str = "Medio"):
        super().__init__(name, price)
        self.sweet_level = sweet_level

    def __str__(self) -> str:
        return f"{self.name} [Dulzura: {self.sweet_level}] - ${self.price:,.0f} COP"


class Order:
    def __init__(self):
        self.items: list[tuple[MenuItem, int]] = []

    def add_item(self, item: MenuItem, quantity: int = 1):
        self.items.append((item, quantity))

    def calculate_total(self) -> float:
        total = sum(item.calculate_total(qty) for item, qty in self.items)
        # Descuento: 10% si la orden supera 150.000 COP
        if total > 150000:
            total *= 0.9
        return total

    def __str__(self) -> str:
        details = "Orden del cliente:\n"
        for item, qty in self.items:
            details += f"{qty} x {item} = ${item.calculate_total(qty):,.0f} COP\n"
        details += f"TOTAL: ${self.calculate_total():,.0f} COP\n"
        return details

if __name__ == "__main__":
    menu = [
        Beverage("Vino Tinto Chianti", 28000, "Copa"),
        Beverage("Agua Mineral San Pellegrino", 12000, "Botella"),
        Beverage("Espresso", 8000, "Taza"),
        Appetizer("Bruschetta", 18000, "3 piezas"),
        Appetizer("Carpaccio de Res", 35000, "Entrada"),
        Appetizer("Ensalada Caprese", 22000, "Individual"),
        MainCourse("Spaghetti alla Carbonara", 42000, False),
        MainCourse("Risotto ai Funghi", 46000, True),
        MainCourse("Lasagna alla Bolognese", 48000, False),
        MainCourse("Pizza Margherita", 39000, True),
        Dessert("Tiramisù", 20000, "Medio"),
        Dessert("Cannoli Siciliani", 18000, "Alto"),
        Dessert("Panna Cotta", 19000, "Bajo"),
    ]

    print("\n=== Menú del Restaurante Italiano ===\n")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")

    order = Order()

    while True:
        choice = input("Selecciona un número del menú (o 'q' para terminar): ")
        if choice.lower() == "q":
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(menu):
                qty = int(input("Cantidad: "))
                order.add_item(menu[idx], qty)
                print("Ítem agregado.\n")
            else:
                print("Opción no válida.\n")
        except ValueError:
            print("Entrada inválida.\n")

    print("\n=== Factura ===\n")
    print(order)
