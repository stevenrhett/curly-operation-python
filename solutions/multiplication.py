# Write a function to find the product (multiplication) of two given numbers only using addition. For example, `multiple(2, 5)` should result in 10.

def multiply(x, y):
    product = 0
    for i in range(x):
        if y > 0:
            product = product + 5

    return product


x = 2
y = 5
product = multiply(x, y)
print(product)
