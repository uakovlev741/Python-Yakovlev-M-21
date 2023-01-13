bibl = set()
N = int(input())
task = set()
M = int(input())
for i in range(N):
    book = input()
    bibl.add(book)
for i in range(M):
    book = input()
    task.add(book)
    if book in bibl:
        print('YES')
    else:
        print('NO')