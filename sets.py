variable = set([1, 2, 3, 4])

print(variable)
print(type(variable))
print(1 in variable)

variable2 = set([1, 2, 3, 3, 4, 5, 6])

print(variable2)
print(variable | variable2)
print(variable & variable2)
print(variable - variable2)
print(variable2 - variable)
print(variable ^ variable2)

variable.add(10)
print(variable)

variable.discard(10)
print(variable)

variable.remove(4)
print(variable)

variable.add(10)
variable.add(9)
variable.add(12)
variable.add(15)
variable.pop
print(variable)

variable.clear
print(variable)