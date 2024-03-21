printCars = {
    "Tesla Model X 80.000$ (1)":"80,000",
    "Tesla Model Y 42,000$ (2)":"42,000",
    "Tesla Model S 95,000$ (3)":"95,000", 
    "Tesla Model S Plaid 110,000$ (4)":"110,000",
    "Tesla Model 3 Refresh 42,000$ (5)":"42,000",
    "Tesla Roadster 150,000$ (6)":"150,000",
    "Tesla Cybertruck 82,000$ (7)":"82,000",
    "Porsche 911 GT3 RS 276,000$ (8)": "276,000"
}

cars = {
    "Tesla Model X":"80,000",
    "Tesla Model Y":"42,000",
    "Tesla Model S":"95,000", 
    "Tesla Model S Plaid":"110,000",
    "Tesla Model 3 Refresh":"42,000",
    "Tesla Roadster":"150,000",
    "Tesla Cybertruck":"82,000",
    "Porsche 911 GT3 RS": "276,000"
}

currency = "280.000"

print("List of available cars:\n", )
for car in printCars:
    print(car)

input = input("\nSelect a car by typing the number displayed next to it: ")

if input == "1":
    if currency >= "80.000":
        print(f"{list(cars.keys())[0]} obtained for {list(cars.values())[0]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "2":
    if currency >= "42,000":
        print(f"{list(cars.keys())[1]} obtained for {list(cars.values())[1]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "3":
    if currency >= "95,000":
        print(f"{list(cars.keys())[2]} obtained for {list(cars.values())[2]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "4":
    if currency >= "110,000":
        print(f"{list(cars.keys())[3]} obtained for {list(cars.values())[3]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "5":
    if currency >= "42,000":
        print(f"{list(cars.keys())[4]} obtained for {list(cars.values())[4]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "6":
    if currency >= "150,000":
        print(f"{list(cars.keys())[5]} obtained for {list(cars.values())[5]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "7":
    if currency >= "82,000":
        print(f"{list(cars.keys())[6]} obtained for {list(cars.values())[6]}$!")
    else:
        print("Not enough money! You can try buying another car.")
elif input == "8":
    if currency >= "276,000":
        print(f"{list(cars.keys())[7]} obtained for {list(cars.values())[7]}$!")
    else:
        print("Not enough money! You can try buying another car.")