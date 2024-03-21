from random import randint

επιλογές = ["Πέτρα", "Ψαλίδι", "Μολύβι", "Χαρτί"]

computer = επιλογές[randint(0,3)]

player = False

while player == False:
    player = input("Διάλεξε Πέτρα, Ψαλίδι, Μολύβι ή Χαρτί: ")
    if player == computer:
        print("Ισοπαλία!")
    elif player == "Πέτρα":
        if computer == "Ψαλίδι":
            print("Κέρδισες!")
        else:
            print("Έχασες!")
    elif player == "Πέτρα":
        if computer == "Μολύβι":
            print("Κέρδισες!")
        else:
            print("Έχασες!")
    elif player == "Πέτρα":
        if computer == "Χαρτί":
            print("Έχασες!")
        else:
            print("Κέρδισες!")
    elif player == "Ψαλίδι":
        if computer == "Μολύβι":
            print("Κέρδισες")
        else:
            print("Έχασες!")
    elif player == "Ψαλίδι":
        if computer == "Χαρτί":
            print("Κέρδισες!")
        else:
            print("Έχασες!")
    elif player == "Μολύβι":
        if computer == "Χαρτί":
            print("Κέρδισες!")
        else:
            print("Έχασες!")
    elif player == "Ψαλίδι":
        if computer == "Πέτρα":
            print("Έχασες!")
        else:
            print("Κέρδισες!")
    elif player == "Μολύβι":
        if computer == "Πέτρα":
            print("Έχασες!")
        else:
            print("Κέρδισες!")
    elif player == "Χαρτί":
        if computer == "Πέτρα":
            print("Κέρδισες!")
        else:
            print("Έχασες!")
    elif player == "Μολύβι":
        if computer == "Ψαλίδι":
            print("Έχασες!")
        else:
            print("Κέρδισες!")
    elif player == "Χαρτί":
        if computer == "Ψαλίδι":
            print("Έχασες!")
        else:
            print("Κέρδισες!")
    elif player == "Χαρτί":
        if computer == "Μολύβι":
            print("Έχασες!")
        else:
            print("Κέρδισες!")
    else:
        print("Γράψε σωστά την επιλογή σου (π.χ. Κεφαλαία, τόνους κλπ.)!")

    player = False
    computer = επιλογές[randint(0,3)]