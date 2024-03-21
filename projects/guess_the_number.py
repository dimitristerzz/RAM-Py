import random

start_number = 1
end_number = 10

random_number = random.randint(start_number, end_number)

while 1 == 1:
    guess = int(input("Συμπλήρωσε έναν αριθμό μεταξύ του 1 και του 10: "))

    if guess == random_number:
        print("Σωστά!")
    else:
        print("Λάθος!")