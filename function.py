def name():
    print("1")
    print("2")
    print("3")

#name()


def add(number1, number2):
    print(number1 + number2)
    
#add(number1= 1, number2= 2)


def circleArea(radius, p=3.14):
    area = (p*radius*radius)
    return area

#a = circleArea(10)
#print(a)


def circle(radius):
    area = 3.14 * radius * radius
    perimeter = 3.14 * 2 * radius
    return area, perimeter

emvado, perimeter = circle(10)
#print(area)
#print(perimeter)


numbers = [1, 2, 3, 4, 5]

def sumNumbers(numbers):
    finalNumber = 0
    for number in numbers:
        finalNumber = finalNumber + number
    return finalNumber

#print(sumNumbers(numbers))


duplicates = [1, 1, 1, 2, 3, 3, 4, 4, 6, 6, 7]

def removeDuplicates(duplicates):
    newList = []
    for element in duplicates:
        if element not in newList:
            newList.append(element)
    return newList

duplicates = removeDuplicates(duplicates)
#print(duplicates)


count = 5

def adittion():
    global count
    count = count + 1
    print(count)

adittion()