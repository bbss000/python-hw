'''
Assignment: B01
Name:許秉森
學號:114502018
系級:資工1B
'''

hunter_name, hunter_year, hunter_height = input().split(',')#輸入時以逗號隔開獵人姓名年齡身高
hunter_lis = input()  
hunter_year_f = float(hunter_year)     #將資料從str轉成float
hunter_height_f = float(hunter_height) 
print("姓名:",hunter_name.strip()) 
print("年齡:",int(hunter_year_f)) #將資料從float轉成int
print("身高:",int(hunter_height_f))       
print("獵人執照:",hunter_lis) 

