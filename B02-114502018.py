'''
Assignment: B02
Name:許秉森
學號:114502018
系級:資工1B
'''

num = input()
num = int(num) #將資料型態轉成int
if(num % 4==0) and (num % 5==0): #可被四與五同時整除
    print('LIGHTNING BOLT')
elif(num % 5 == 0): #可被五整除
    print('LIGHTNING')
elif(num % 4==0) :#可被四整除
    print('FIRE')
else:#不可被四或五整除
    print(num)