pass1 = input()
pass2 = input()
while len(pass1) < 8:
    print("Короткий!")
    pass1 = input()
    pass2 = input()
while "123" in pass1:
    print("Простой!")
    pass1 = input()
    pass2 = input()
while pass2 != pass1:
    print("Различаются.")
    pass1 = input()
    pass2 = input()
else:
    print("OK")
