a = int(input('Введите число: '))
b = int(input('Введите число, больше предыдущего: '))
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)