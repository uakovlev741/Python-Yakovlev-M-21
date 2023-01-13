n = int(input())
for j in range(n):
    txt = input()
    for i in txt:
        if txt[:4] == '####':
            continue
        elif txt[:2] == '%%':
            print(txt[2:])
            break
        else:
            print(txt)
            break