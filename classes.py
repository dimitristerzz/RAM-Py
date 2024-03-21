class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discount(self, rate):
        self.price = self.price - (self.price*(rate/100))

    def provideInfo(self):
        self.name = input("Pleast provide the name of the product you want me to print: ")
        self.price = int(input("Pleast provide the price of the product you want me to print: "))

    def pullInfo(self):
        print(self.name, self.price)

'''car = Product("", "")
car.provideInfo()
car.discount(10)
car.pullInfo()'''


class DigitalProduct(Product):
    category = "Digital"

    def __init__(self, link):
        self.link = link
    
    def provideLink(self):
        self.link = input("Pleast provide the link of the product you want me to print: ")

    def pullLink(self):
        print(self.link)

    def info(cls):
        print(f"This method is in the {cls.category} category.")


ebook = DigitalProduct("")
ebook.provideInfo()
ebook.provideLink()
ebook.pullLink()
ebook.info()