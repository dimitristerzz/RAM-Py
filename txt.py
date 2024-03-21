'''
file = open('C:/Users/dterz/OneDrive/Documents/RAM/components/txt.txt', 'r')

data = file.read()
print(data)

data = file.read(10)
print(data)

data = file.readline()
print(data)
'''


'''
file = open('C:/Users/dterz/OneDrive/Documents/RAM/components/txt.txt', 'w')

file.write('HELLO WORLD')
file.close()
'''


'''
file = open('C:/Users/dterz/OneDrive/Documents/RAM/components/txt.txt', 'a')

content = '\n Hello World'

file.write(content)
file.close()
'''


'''
with open('C:/Users/dterz/OneDrive/Documents/RAM/components/txt.txt', 'r') as file:
    content = file.read()
    print(content)
'''


'''
with open('C:/Users/dterz/OneDrive/Documents/RAM/components/txt.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()

print("Line 1:", line1)
print("Line 2:", line2)
'''


with open('C:/Users/dterz/OneDrive/Documents/RAM/components/txt.txt', 'r') as file:
    lines = file.readlines()


for line in lines:
    print(line)