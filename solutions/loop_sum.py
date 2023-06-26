# Write a program to calculate the sum of digits in a number using a loop.

def main():
    number = int(input("Enter a number: "))
    sum = 0
    while number > 0:

        sum = sum + number % 10  # 7  set - assign
        # sum += number % 10   # 17 - 10
        number //= 10
        # number = number // 10 cutting off last digit
        # double slash (//) rounds down
        # loop until the conditon of the while is met
    print(sum)

    # pick two random numbers and one operator and other multivariable problems
    # loops problems and data parsing problems
