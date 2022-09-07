'''
行ごとの2次元配列を持つ行クラス
'''
class Row():
    # 行ごとの配列
    row_array = [[]]
    question_array = [[]]

    '''
    コンストラクタ
        配列の初期化
    '''
    def __init__(self):
        # 9 * 9の配列を全て0で埋める
        self.row_array = [[0 for i in range(1, 10)] for j in range(1, 10)]
        self.question_array = [[0 for i in range(1, 10)] for j in range(1, 10)]

    '''
    セッター
    添字を指定して行ごとにセットする
        array: セットする1次元配列
        index: セットしたい位置の添字
    '''
    def set_array(self, array, index):
        self.row_array[index] = array
    
    '''
    ゲッター
    行ごとにゲットする
        index: ゲットしたい位置の添字
    '''
    def get_array(self, index):
        return self.row_array[index]

    '''
    問題配列をゲットするメソッド
        index: 配列の添字
        return: 問題の配列
    '''
    def get_question(self, index):
        return self.question_array[index]

    '''
    問題配列を初期化するメソッド
    '''
    def initialize_question(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.question_array[i][j] = self.row_array[i][j]

    '''
    配列をリセットするメソッド
    '''
    def reset(self):
        self.row_array = [[0 for i in range(1, 10)] for j in range(1, 10)]

    '''
    問題配列に穴をあけるメソッド
        row_hole: 行
        column_hole: 列
    '''
    def make_hole(self, row_hole, column_hole):
        self.question_array[column_hole][row_hole] = "?"

    '''
    問題配列に答えを埋めるメソッド
        row_hole: 行
        column_hole: 列
    '''
    def fill_hole(self, row_hole, column_hole):
        self.question_array[column_hole][row_hole] = self.row_array[column_hole][row_hole]

    '''
    入力された解答が正しいか確認するメソッド
        row_hole: 行
        column_hole: 列
        value: 値
        return: 正解、不正解
    '''
    def check_hole(self, row_hole, column_hole, value):
        # 正解、かつ問題箇所に正解が入力された場合
        if(self.row_array[column_hole][row_hole] == value and self.question_array[column_hole][row_hole] == "?"):
            return True
        else:
            return False
