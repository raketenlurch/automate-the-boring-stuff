def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        return number

# Version 1
try:
    num = int(input('Please enter a number:'))
    while num != 1:
        print(collatz(num))
        num = num - 1
except ValueError:
    print('Value must be an Integer.')

# Version 2
#num = int(input('Please enter a number:'))
#while num != 1:
#    print(collatz(num))
#    num = num - 1
