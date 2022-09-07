import sudoku_class
'''
実行ファイル
'''

# 数独インスタンス作成
sudoku_question = sudoku_class.Sudoku()
# 解答作成
sudoku_question.generate()

# 難易度
difficulty = 6
# 難易度を1 ~ 6から入力
while True:
    i = input("難易度を入力(1 ~ 6)>>>")
    if i.isdecimal() and 1 <= int(i) <= 6:
        i = int(i)
        difficulty = i
        break
    print("入力が正しくありません")

# 難易度 * 10のマス数を開ける
difficulty *= 10
sudoku_question.make_question(difficulty)
# 問題表示
sudoku_question.show()

# 答え入力
column = "a"
row = "A"
# 埋めるマスが0になるまで
while difficulty > 0:
    while True: # 入力行列が正当か
        column = input("列を小文字アルファベットで入力>>>")
        row = input("列を大文字アルファベットで入力>>>")
        value = input("数字を入力>>>")
        if 0 <= ord(column) - 97 <= 8 and 0 <= ord(row) - 65 <= 8:
            break
        print("入力が正しくありません")
    # 正解の場合マス数減らす    
    if(sudoku_question.answer(column, row, int(value))):
        difficulty -= 1

print("クリア")
