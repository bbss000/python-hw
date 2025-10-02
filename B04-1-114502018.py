'''
Assignment: B04-1
Name:許秉森
學號:114502018
系級:資工1B
'''
sudoku_board = []  # 用來儲存數獨盤面
for row_index in range(9):
    row = list(input())  # 讀取每一列並轉成字元串列
    sudoku_board.append(row)  # 加入盤面

# 檢查每一行是否有重複數字
def Check_Rows(board):
    for row_index in range(9):         # 逐行
        for col_index in range(9):     # 逐欄
            for next_row in range(row_index + 1, 9):  # 與同一欄其他行比較
                if str(board[row_index][col_index]) != '.' and board[row_index][col_index] == board[next_row][col_index]:
                    return False      # 有重複就回傳 False
    return True                      # 沒有重複回傳 True

# 檢查每一列是否有重複數字
def Check_Columns(board):
    for col_index in range(9):         # 逐欄
        for row_index in range(9):     # 逐行
            for next_col in range(col_index + 1, 9):  # 與同一行其他欄比較
                if str(board[row_index][col_index]) != '.' and board[row_index][col_index] == board[row_index][next_col]:
                    return False      # 有重複就回傳 False
    return True                      # 沒有重複回傳 True

# 檢查每個 3x3 九宮格是否有重複數字
def Check_Subgrids(board):
    for row_index in range(9):         # 逐行
        for col_index in range(9):     # 逐欄
            cell_value = board[row_index][col_index]  # 目前格子的值
            # 計算目前格子所在九宮格的起始行和起始欄
            start_row = row_index - row_index % 3
            start_col = col_index - col_index % 3
            for sub_row in range(start_row, start_row + 3):      # 九宮格的行範圍
                for sub_col in range(start_col, start_col + 3):  # 九宮格的欄範圍
                    if row_index == sub_row and col_index == sub_col:
                        continue      # 跳過自己
                    if cell_value == board[sub_row][sub_col] and str(cell_value) != '.':
                        return False  # 有重複就回傳 False
    return True                      # 沒有重複回傳 True

# 三種檢查都通過才輸出「好耶」，否則輸出「不好耶」
if Check_Columns(sudoku_board) and Check_Rows(sudoku_board) and Check_Subgrids(sudoku_board):
    print('好耶')
else:
    print('不好耶')
