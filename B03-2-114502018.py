'''
Assignment: B03-2
Name:許秉森
學號:114502018
系級:資工1B
'''
num_chars = int(input())  # 讀取輸入的字元數量
char_list = input().split(' ')  # 讀取字元並以空格分割成串列
swap_count = 0  # 用來計算交換次數

# 外層迴圈，控制排序的輪數
for i in range(0, num_chars + 1, 1): 
    # 內層迴圈，進行相鄰元素比較與交換
    for j in range(0, num_chars + 1, 1):
        if j + 1 < num_chars:  # 確保不超出索引範圍
            if ord(char_list[j]) > ord(char_list[j + 1]):  # 如果前一個字元的ASCII值大於後一個
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]  # 交換兩個字元
                swap_count += 1  # 交換次數加一

# 輸出排序後的字元
for i in range(0, num_chars, 1):
    if i < num_chars - 1:
        print(chr(ord(char_list[i])), end=' ')  # 不是最後一個字元就加空格
    elif i == num_chars - 1:
        print(chr(ord(char_list[i])))  # 最後一個字元換行

# 輸出交換次數
print('swaps=', end = '')
print(swap_count)