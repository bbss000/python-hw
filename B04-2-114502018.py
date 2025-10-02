'''
Assignment: B04-2
Name:許秉森
學號:114502018
系級:資工1B
'''
'''
data_file = open('dictionary.txt', 'r')  # 開啟 dictionary.txt 檔案，讀取模式
output_file = open('output.txt','w')     # 開啟 output.txt 檔案，寫入模式
for line in data_file:                   # 逐行讀取 dictionary.txt 的內容
    word = line.split(',')               # 以逗號分割每行，得到單字串列
    print(word, file = output_file)      # 將單字串列寫入 output.txt 檔案
data_file.close()                        # 關閉 dictionary.txt 檔案
output_file.close()                      # 關閉 output.txt 檔案
'''
word_list =input().split(',')
word_count = len(word_list)
# 計算單字總數
def Count_Words(word_list):
    return str(len(word_list))

# 找出最長的單字（可能有多個）
def Find_Longest(word_list):
    longest_words = []         # 用來儲存最長單字
    longest_word = ' '         # 初始最長單字（長度為0）
    for i in range(word_count):
        if len(word_list[i]) == len(longest_word):  # 如果長度相同，加入結果
            longest_words.append(word_list[i])
        elif len(word_list[i]) > len(longest_word): # 如果更長，清空結果並加入新單字
            longest_words = []
            longest_words.append(word_list[i])
            longest_word = word_list[i]
    for i in range(len(longest_words)):
        longest_words[i] = (longest_words[i], len(longest_words[i]))  # 以(單字,長度)格式儲存
    return longest_words

# 找出最短的單字（可能有多個）
def Find_Shortest(word_list):
    shortest_words = []           # 用來儲存最短單字
    shortest_word = word_list[0]  # 初始最短單字
    for i in range(word_count):
        if len(word_list[i]) == len(shortest_word):  # 如果長度相同，加入結果
            shortest_words.append(word_list[i])
        elif len(word_list[i]) < len(shortest_word): # 如果更短，清空結果並加入新單字
            shortest_words = []
            shortest_words.append(word_list[i])
            shortest_word = word_list[i]
    for i in range(len(shortest_words)):
        shortest_words[i] = (shortest_words[i], len(shortest_words[i]))  # 以(單字,長度)格式儲存
    return shortest_words

# 輸出結果
print('總共有' + Count_Words(word_list) + '個單字')
print('最長的單字有:')
print(Find_Longest(word_list))
print('最短的單字有:')
print(Find_Shortest(word_list))

