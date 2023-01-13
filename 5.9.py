n = int(input())
catflag = False
for i in range(n):
    fraza = input()
    if 'Кот' in fraza or 'кот' in fraza:
        flagcat = True
    elif 'Пёс' in fraza or 'пёс' in fraza:
        catflag = False
if catflag is True:
    print('МЯУ')
elif catflag is False:
    print('НЕТ')