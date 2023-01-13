n = int(input())
flag = False
nums = list()
for i in range(n):
    nums.append(int(input()))
m = int(input())
for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] * nums[j] == m:
            flag = True
            break
if flag:
    print("Да")
else:
    print("Нет")
