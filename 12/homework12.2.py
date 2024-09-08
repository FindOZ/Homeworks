class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price} UAH"

class Customer:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return f"Customer: {self.last_name} {self.first_name}, Phone: {self.phone_number}"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def __str__(self):
        order_details = [f"{product.name} (x{quantity}) - {product.price * quantity} UAH"
                         for product, quantity in self.items.items()]
        return f"Order by {self.customer}:\n" + "\n".join(order_details) + f"\nTotal: {self.total_price()} UAH"

def input_product():
    name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    return Product(name, price)

def input_customer():
    first_name = input("Введіть ім'я покупця: ")
    last_name = input("Введіть прізвище покупця: ")
    phone_number = input("Введіть телефон покупця: ")
    return Customer(first_name, last_name, phone_number)

customer1 = input_customer()

order1 = Order(customer=customer1)

while True:
    product = input_product()
    quantity = int(input(f"Введіть кількість для {product.name}: "))
    order1.add_product(product, quantity)

    continue_choice = input("Додаєте ще один товар? (так/ні): ")
    if continue_choice.lower() != "так":
        break

print(order1)
