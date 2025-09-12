'''
Assignment 01
Name:許秉森
Student Number:114502018
Course 2025-CE1003B-資工一B
'''
hunter_name, hunter_year, hunter_height = input('請輸入獵人姓名，年齡，身高').strip().split(',')#輸入時以逗號隔開獵人姓名年齡身高
hunter_lis = input("是否持有獵人執照")  
hunter_year_f = float(hunter_year)     #將資料從str轉成float
hunter_height_f = float(hunter_height) 
print("姓名：",hunter_name.strip()) 
print("年齡：",int(hunter_year_f)) #將資料從float轉成int
print("身高：",int(hunter_height_f))       
print(f'獵人執照：{"True" in hunter_lis}') #判別hunter_lis是否輸入True

