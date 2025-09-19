'''
Assignment: B03-1
Name:許秉森
學號:114502018
系級:資工1B
'''
input_str = input()  # 讀取輸入字串
str_len = len(input_str)   # 計算字串長度
longest_palindrome = ' '   # 用來儲存最長的回文子字串，初始為空白

# 第一層：尋找奇數長度的回文子字串
for center in range(0, str_len, 1):
    for offset in range(0, str_len // 2 + 1, 1):
        if center - offset >= 0 and center + offset < str_len:  # 確保索引不超出範圍
            if input_str[center - offset] == input_str[center + offset]:  # 檢查對稱位置的字元是否相同
                if len(longest_palindrome) < len(input_str[center - offset:center + offset]):
                    longest_palindrome = input_str[center - offset:center + offset + 1]  # 更新最長回文子字串
            else:
                break  # 若不相同則跳出內層迴圈

# 第二層：尋找偶數長度的回文子字串
for center in range(0, str_len, 1):
    for offset in range(0, str_len // 2 + 1, 1):
        if center - offset >= 0 and center + offset < str_len:  # 確保索引不超出範圍
            if input_str[center - offset - 1] == input_str[center + offset]:  # 檢查對稱位置的字元是否相同
                if len(longest_palindrome) < len(input_str[center - offset - 1:center + offset]):
                    longest_palindrome = input_str[center - offset - 1:center + offset + 1]  # 更新最長回文子字串
            else:
                break  # 若不相同則跳出內層迴圈

# 輸出結果
if longest_palindrome != ' ':
    print(longest_palindrome)  # 輸出最長回文子字串
else:
    print('No Palindrome')  # 若沒有回文則輸出提示