a=int(input())
b=int(input())
c=[i for i in range(1,a+1)]
d=[]
e=[]
f=[]
for i in range(b):
    h,r=input().split(',')
    r = int(r)
    if not h.isdigit(): 
        f.append('錯誤: 座號不可包含文字')
        continue
    if r<0:
        f.append('錯誤: 簽到時間不可為負數')
        continue
    if int(r) > 30 and int(h) in c:
        e.append(int(h))
    if int(h)  in c and r>=0:
        c.remove(int(h))
    elif int(h) not in c:
        if int(h) not in d and int(h)<=a :
            d.append(int(h))
        if int(h) in e:
            e.remove(int(h))
c.sort()
d.sort()
e.sort()
for i in range(len(f)):
    print(f[i])
if len(c) != 0:
    print('沒來的學生:',end ='')
else:
    print('沒來的學生:')
for i in range(len(c)):
    if i != len(c)-1:
        print(c[i],end=',')
    else:
        print(c[i])
if len(e) != 0:
    print('遲到的學生:',end ='')
else:
    print('遲到的學生:')
for i in range(len(e)):
    if i != len(e)-1:
        print(e[i],end=',')
    else:
        print(e[i])
if len(d) != 0:
    print('有代簽的學生:',end ='')
else:
    print('有代簽的學生:')
for i in range(len(d)):
    if i != len(d)-1:
        print(d[i],end=',')
    else:
        print(d[i])