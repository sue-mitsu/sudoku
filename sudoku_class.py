import random
import row, column, box
import string
'''
数独クラス
'''

class Sudoku():
    row_class = None
    column_class = None
    box_class = None

    '''
    コンストラクタ
    変数の初期化
    '''
    def __init__(self):
        self.row_class = row.Row()
        self.column_class = column.Column()
        self.box_class = box.Box()

    '''
    解答作成メソッド
    数秒かかる可能性あり
    '''
    def generate(self):
        print("作成開始...")
        # 回数保存のため
        reset_counter = 0
        shuffle_counter = 0
        # 列数カウント
        column_num = 0

        # 9列全て作成し終えるまで
        while column_num < 9:
            # 1 ~ 9 の配列をランダムに作成
            shuffle_array = [i for i in range(1, 10)]
            random.shuffle(shuffle_array)

            # 数独のルールに乗っ取るまでシャッフル
            for redo in range(0, 100000):
                shuffle_counter += 1
                # 列のルールとボックスのルール確認
                if not self.column_class.available_column_values(shuffle_array) or not self.box_class.available_box_values(shuffle_array, column_num):
                    # やり直し
                    random.shuffle(shuffle_array)
                else:
                    # ルールに則ったのでその行を設定
                    self.row_class.set_array(shuffle_array, column_num)
                    self.column_class.set_array(shuffle_array, column_num)
                    self.box_class.set_array(shuffle_array, column_num)
                    column_num += 1
                    break
            else: # 100000回でうまく行かない時すべてリセットしてやり直す
                reset_counter += 1
                column_num = 0
                self.row_class.reset()
                self.column_class.reset()
                self.box_class.reset()
            
            # for i in range(0, 9):
            #     print(self.row_class.get_array(i))   
            # print( "-----------------------------------")
        print("作成完了\nリセット数:", reset_counter, "シャッフル数:", shuffle_counter)
   
    '''
    表示メソッド
    '''
    def show(self):
        print()
        character = "    "

        # 大文字を行に沿って表示
        for i in range(0, 9):
            character += list(string.ascii_uppercase)[i]
            character += "   "
        print(character)
        # 一番上
        print("  +===========+===========+===========+ ")

        # 数値を文字列にして表示
        for i in range(0, 9):
            # 小文字を列に沿って表示
            print(list(string.ascii_lowercase)[i], end = " ")
            message = "| "
            for j in range(0, 9):
                message += str(self.row_class.get_question(i)[j])
                message += " | "
            print(message)
            # 3の倍数の時ボックスを見やすくするため表示切り替え
            if (i + 1) % 3 == 0:
                print("  +===========+===========+===========+ ")
            else:    
                print("  +-----------|-----------|-----------+ ")
        print(character)
        print()

    '''
    問題作成メソッド
        difficulty: 難易度（穴をあける数）
    '''
    def make_question(self, difficulty):
        # 問題配列に正解配列を代入
        self.row_class.initialize_question()

        # ランダムに穴をあける
        for i in range(0, difficulty):
            row_hole = random.randint(0, 8)
            column_hole = random.randint(0, 8)
            self.row_class.make_hole(row_hole, column_hole)
            
    '''
    解答を入力し、正解か否かを判別するメソッド
        lower: 小文字（列）
        upper: 大文字（行）
        value: 数値
        return: 正解、不正解
    '''
    def answer(self, lower, upper, value):
        # 行列を数値に変換
        column = ord(lower) - 97
        row = ord(upper) - 65
        
        # 解答の数値が正解か確認
        if(self.row_class.check_hole(row, column, value)):
            print("正解")
            # 解答を埋める
            self.row_class.fill_hole(row, column)
            self.show()
            return True
        else:
            print("不正解")
            return False
        
        
