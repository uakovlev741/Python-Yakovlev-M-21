print('Отвечайте только Да или Нет!!!')
answer_1 = input('Вы любите котиков?: ')
answer_2 = input('Умеете ли вы програмировать?: ')
if answer_1 == 'Да' and answer_2 == 'Да':
    print('Вы молодец')
elif answer_1 == 'Нет' and answer_2 == 'Да':
    print('У вас незаурядный ум')
elif answer_1 == 'Нет' and answer_2 == 'Нет':
    print('Нам не о чем с тобой разговаривать!')
elif answer_1 == 'Да' and answer_2 == 'Нет':
    print('Вроде плохо, а вроде нет')
else:
    print('Ошибка, посмотрите выше!!!')