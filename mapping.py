numbers = [1, 2, 3, 4, 5]
def square(x):
    return x*x

# for number in numbers:
#     print(square(number))

new_numbers = list(map(square, numbers))
print(new_numbers)