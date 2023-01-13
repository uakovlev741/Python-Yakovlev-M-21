pass1 = input('Введите пароль: ')
pass2 = input('Повторите пароль: ')
if pass1 != pass2:
    print('Пароли различаются!!!')
elif len(pass1) < 8:
    print('Пароль короткий')
else:
    print('Ok')