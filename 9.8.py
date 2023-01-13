n = int(input())
list = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
for i in range(n):
    print(list[i % 5])

