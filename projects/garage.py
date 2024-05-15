cars = {
    "Alfa Romeo 8C Competizione": 306380,
    "Alfa Romeo 33 Stradale": 1220000,
    "Alfa Romeo Giulia Quadrifoglio": 89750,
    "Audi RS3": 75100,
    "Bentley Continental GT": 245340,
    "BMW 2 Series": 39040,
    "BMW 4 Series": 74650,
    "BMW 5 Series": 59960,
    "BMW 7 Series": 98900,
    "BMW i4": 70200,
    "BMW i5": 106250,
    "BMW i7": 169370,
    "BMW iX": 112010,
    "BMW M2": 65120,
    "BMW M3": 77400,
    "BMW M4": 80560,
    "BMW M8": 235540,
    "BMW X1": 42240,
    "BMW X2": 45630,
    "BMW X3 M": 84230,
    "BMW X5 M": 102630,
    "BMW X6": 75530,
    "BMW X6 M": 198850,
    "BMW XM": 192950,
    "Cadillac Escalade IQ": 130080,
    "Corvette C8 Z06": 114880,
    "Corvette E-Ray": 105900,
    "Ferrari 250 GTO": 70256200,
    "Ferrari 296GTB": 376210,
    "Ferrari 488 GTB": 300400,
    "Ferrari F12berlinetta": 245200,
    "Ford F150 Matte Black": 98450,
    "Hyundai Ioniq 6": 51150,
    "Infiniti QX80": 77140,
    "Jaguar XJR": 123100,
    "Kia EV6 GT": 63000,
    "Kia EV9": 84260,
    "Lamborghini Aventador SVJ": 600400,
    "Lamborghini Estoque": 230450,
    "Lamborghini Gallardo": 127200,
    "Lamborghini Murcielago": 235500,
    "Lamborghini Reventón": 1400870,
    "Lamborghini Sesto Elemento": 2920000,
    "Lamborghini Sterrato": 232800,
    "Lamborghini Urus": 273120,
    "Lamborghini Veneno": 10207000,
    "Lexus IS500": 59530,
    "Lotus 3-Eleven": 115200,
    "Lotus Eletre": 115452,
    "Lotus Elise Cup 220": 68300,
    "Lotus Elise GT1": 645340,
    "Lotus Emeya": 165320,
    "Lotus Esprit Sport 300": 80260,
    "Lotus Evija": 2322000,
    "Lotus Evora GT": 99500,
    "Lotus Exige S Type 72": 36050,
    "Lotus Exige Sport 410": 106520,
    "Lotus Sport Exige 240R": 59250,
    "Lucid Air": 71250,
    "Lucid Gravity": 80100,
    "Maserati GranTurismo": 160400,
    "Mazda CX-90": 40210,
    "McLaren 570S Coupe": 192500,
    "McLaren 600LT": 259500,
    "McLaren 675LT": 259900,
    "McLaren 720S": 336580,
    "McLaren F1": 800410,
    "McLaren M12": 90590,
    "McLaren P1": 1100600,
    "McLaren Senna": 825500,
    "Mercedes G63 AMG": 179320,
    "Mercedes EQS SUV": 136700,
    "Mustang 2": 50100,
    "Polestar 2": 51300,
    "Porsche 356": 590000,
    "Porsche 550 Spyder": 5170000,
    "Porsche 911 Carrera S": 197140,
    "Porsche 911 GT3 R Hybrid 2.0": 1046000,
    "Porsche 911 GT3 RS": 380230,
    "Porsche 911 S/T": 292000,
    "Porsche 911 Speedster Concept": 211599,
    "Porsche 911 Sport Classic 997": 390000,
    "Porsche 944 S2": 39500,
    "Porsche Cayenne Turbo": 139090,
    "Porsche Cayman GTS 981": 63243,
    "Porsche Macan T": 109350,
    "Porsche Macan Turbo": 102410,
    "Porsche Panamera Turbo S E-Hybrid": 154570,
    "Porsche Porsche 911 Turbo Flachbau 930": 204677,
    "Rezvani Beast": 385000,
    "Rimac Nevera": 2220000,
    "Rivian R1S": 76700,
    "Rivian R1T": 71700,
    "Rivian R2": 45100,
    "Rivian R3": 37460,
    "Rolls Royce Spectre": 422750,
    "Subaru BRZ": 30195,
    "Tesla Cybertruck": 81895,
    "Tesla Model 3 Refresh": 47490,
    "Tesla Model S": 74990,
    "Tesla Model S Plaid": 93480,
    "Tesla Model X": 79990,
    "Tesla Model Y": 45630,
    "Tesla Roadster": 43000,
    "Toyota Grand Highlander": 54940,
}

ownedCars = []

for index, (value, key) in enumerate(cars.items(), start=1):
    if index == 1:
        print(f"List of available cars: \n({index}) {value}: {key:,}$")
    else:
        print(f"({index}) {value}: {key:,}$")

balance = 5315612

print(f"\nYour current balance is: {balance:,}$")

first_attempt = True

def logic():
    global balance
    if balance >= list(cars.values())[choice - 1]:
        print(f"\nObtained \"{list(cars.keys())[choice - 1]}\" for {list(cars.values())[choice - 1]:,}$!")
        for index, (value, key) in enumerate(cars.items(), start=1):
            if index == 1:
                print(f"\nNew list: \n({index}) {value}: {key:,}$")
            else:
                print(f"({index}) {value}: {key:,}$")
        balance = balance - int(list(cars.values())[choice - 1])
        print(f"\nNew balance: {balance:,}$")
        ownedCars.append(list(cars.keys())[choice - 1])
        cars.pop(list(cars.keys())[choice - 1])
        print(f"\nOwned cars: {", ".join(ownedCars)}")
        
    else:
        print("Insufficient balance, please select another car by typing the number displayed next to it: ")

while True:
    try:
        if first_attempt:
            choice = int(input("\nSelect a car by typing the number displayed next to it: "))
            logic()
            first_attempt = True
        else:
            choice = int(input("\nPlease provide a valid number: "))
            logic()
            first_attempt = True
    except ValueError:
        first_attempt = False
        pass