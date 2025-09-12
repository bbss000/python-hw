import math

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    x = float(s)

    if math.isnan(x):
        print("NaN")
    elif math.isinf(x):
        print("0")
    elif x == 0.0:
        if s.startswith('-'):
            print("-inf")
        else:
            print("inf")
    else:
        # print reciprocal with about 12 significant digits
        print("{:.12g}".format(1.0 / x))
