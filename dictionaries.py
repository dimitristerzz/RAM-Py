pythonNamesAges1 = {
    "Sotiris":31,
    "Marios":15,
    "Konstantinos":14,
    "Dimitris":15,
    "Giorgos":15,
    "Giorgos":14,
    "Karatzas":15,
    "Konstantinos":14,
}

pythonNamesAges2 = {
    "Sotiris":45,
    "Marios":12,
    "Konstantinos":16,
    "Dimitris":13,
    "Giorgos":11,
    "Giorgos":19,
    "Karatzas":14,
    "Konstantinos":15,
}

pythonNamesAges1.update(pythonNamesAges2)
pythonNamesAges1.pop("Sotiris")
print(pythonNamesAges1)
print(pythonNamesAges1.keys())
print(pythonNamesAges1.values())
print(pythonNamesAges1.items())

'''
pythonNamesAges = dict(
    Sotiris=31,
    Marios=15,
    Konstantinos=14,
    Dimitris=15,
    Giorgos=15,
    Giorgos=14,
    Karatzas=15,
    Konstantinos=14,
)

pythonNamesAges["Giorgos"] = 15
del pythonNamesAges["Marios"]

print(pythonNamesAges.get("Marios"))

pythonNamesAges[]"Dimitris"] = 9

print(mathites.get("Dimitris"))
'''