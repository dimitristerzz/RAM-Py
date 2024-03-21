'''class A:
    def method_a(self):
        print("Method A.")

class B(A):
    def method_b(self):
        print("Method B.")

class C(B):
    def method_c(self):
        print("Method C.")

item = C()
item.method_c()'''


class Food:
    def type(self):
        print("Food")

class Fruit(Food):
    def type(self):
        print("Fruit")

burger = Food()
burger.type()

apple = Fruit()
apple.type()