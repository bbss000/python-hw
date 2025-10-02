a = input().split(',')
b = int(input())
c = len(a)
r = {}


for j, k in enumerate(a):
    if k not in r:
        r[k] = []
    r[k].append(j)

s = []
for i in range(c-1, -1, -1):
    d = str(b - int(a[i]))
    if d in r:
        for j in r[d]:
            if j < i:
                s.append(f"{j},{i}")

for j in range(len(s)-1, -1, -1):
    print(s[j])