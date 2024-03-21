# create a list with tech products
techProducts = ['M3 Max MacBook Pro', 'iPhone 15 Pro Max', 'AirPods Max', 'Apple Watch Ultra', 'iPad Pro']

# print the list
print(f"Products included in the list: {techProducts}")

# ask the user a product to remove
removeProduct = input("Fill in a product to remove from the list (caps sensitive): ")
techProducts.remove(removeProduct)

# print the list
print(f"Products included in the list: {techProducts}")

# ask the user a product to add
addProduct = input("Fill in a product to add to the list (caps sensitive): ")
techProducts.append(addProduct)

# print the list
print(f"Products included in the list: {techProducts}")

# ask again the user a product to add
addProduct = input("Fill in another product to add to the list (caps sensitive): ")

# ask the user after we print the list in which position they want to add the product
print(f"Products included in the list: {techProducts}")
productPositionInput = input("Fill in the position in which you want to add the product: ")
productPosition = techProducts.index(productPositionInput)
techProducts.insert(productPosition, addProduct)

# print the final list
print(techProducts)