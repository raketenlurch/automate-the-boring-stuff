def collatz(number):

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            return number
        elif number == 1:
            return number
        else:
            number = 3 * number + 1
            return number

try:
    num = collatz(int(input('Enter number: ')))
    while num != 1:
        num = collatz(num)
        print(num)
except ValueError:
    print('Value must be an Integer.')
