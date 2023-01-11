message = input()
price = len(message) * 40
rub = price // 100
cop = price % 100
print(rub,'Р', cop, 'Коп')