def even_generator(x):
    for i in range(x):
        if i%2 == 0:
            yield i

# yield returns the result as an object and not as a number
        
print(list(even_generator(10)))