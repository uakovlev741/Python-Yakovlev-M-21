num1 = float(input())
num2 = float(input())
str = input()
if str == '+':
    print(num1 + num2)
elif str == '-':
    print(num1 - num2)
elif str == '*':
    print(num1 * num2)
elif str == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('888888')
else:
    print('888888')