days = 0
while True:
    temp = float(input('Введите температуру: '))
    if temp >= 22.0:
        break
    days += 1
    weeks = days // 7
print(weeks)
