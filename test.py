n = 0
a = 0
while n != 999 :
    n =input()
    n = int(n)
    if (n < 999) and (n > 0):
        a += n
    elif (n == 999):
        print(a)
        break 