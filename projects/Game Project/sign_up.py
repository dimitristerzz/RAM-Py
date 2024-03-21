from username_generator import random_username
from password_generator import random_password

def name_input():
    while True:
        random_username_request = input("Θα θέλατε να παράγω ένα τυχαίο όνομα χρήστη; (Ν/Ο): ")

        if random_username_request == "Ν":
            username = random_username
            print(f"Το όνομα χρήστη σας είναι: {username}")
            break
        elif random_username_request == "Ο":
            username = input("Παρακαλώ συμπληρώστε το όνομα χρήστη σας: ")
            print(f"Το όνομα χρήστη σας είναι: {username}")
            break
        else:
            print("Παρακαλώ απαντήστε με 'Ν' για ναι και με 'Ο' για όχι.")

def password_input():
    while True:
        random_password_request = input("Θα θέλατε να παράγω ένα τυχαίο κωδικό πρόσβασης; (Ν/Ο): ")

        if random_password_request == "Ν":
            password = random_password
            print(f"Ο κωδικός πρόσβασής σας είναι: {password}")
            break
        elif random_password_request == "Ο":
            password = input("Παρακαλώ συμπληρώστε το κωδικό πρόσβασή σας σας: ")
            print(f"Ο κωδικός πρόσβασής σας είναι: {password}")
            break
        else:
            print("Παρακαλώ απαντήστε με 'Ν' για ναι και με 'Ο' για όχι.")

name_input()
password_input()