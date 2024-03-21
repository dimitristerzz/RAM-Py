'''def product():
    name = input("Pleast type the name of the product you want me to add: ")
    price = input("Pleast type the price of the product you want me to add: ")
    print(f"The product's name is {name} and it costs {price}€.")

product()'''


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = name

    def provideInfo(self):
        self.name = input("Pleast type the name of the product you want me to add: ")
        self.price = input("Pleast type the price of the product you want me to add: ")

    def pullInfo(self):
        print(f"The product's name is {self.name} and it costs {self.price}€.")

product = Product("", "")
product.provideInfo()
product.pullInfo()