chars = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
niсk_name = input()
for i in niсk_name:
    if i not in '1234567890_qwertyuiopasdfghjklzxcvbnm':
        print('Неверный символ:', i)
        break
else:
    print('OK')