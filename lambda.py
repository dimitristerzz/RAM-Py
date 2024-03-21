'''
def square(x):
    return x**2

print(square(9))
'''

square = (lambda x: x**2)(9)
print(square)

adittion = (lambda x=10,y=15: x+y)(3,9) #(y=3,x=9) #(3)(9)
print(adittion)