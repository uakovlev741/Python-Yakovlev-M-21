login = input('Введите логин: ')
mail = input('Введите почту: ')
if '@' in login and '@' in mail:
    print('Некоректный логин')
if '@' not in login and '@' not in mail:
    print('Некоректная почта')
else:
    print('Ok')