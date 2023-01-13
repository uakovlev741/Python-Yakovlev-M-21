cat = False
c = 0
phrase = ''
while phrase != 'СТОП':
    phrase = input()
    c += 1
    if ('Кот' in phrase) or ('кот' in phrase):
        cat = True
        n = c
        break
while phrase != 'СТОП':
    phrase = input()
if cat:
    print(n)
else:
    print(-1)