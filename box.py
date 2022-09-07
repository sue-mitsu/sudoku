'''
3 * 3のボックスごとの2次元配列を持つクラス
左上から右に向かって添字順となる
'''
class Box():
    # ボックスごとの配列
    box_array = [[]]

    '''
    コンストラクタ
        変数の初期化
    '''
    def __init__(self):
        # 9 * 9の配列を全て0で埋める
        self.box_array = [[0 for i in range(1, 10)] for j in range(1, 10)]

    '''
    セッター
        列を指定してボックスごとにセットする
        array: セットする1次元配列
        column: セットしたい列
    '''
    def set_array(self, array, column):
        # セットする列を3の倍数に減らす。何度減らしたか覚えておく
        counter = 0
        while column != 0 and column % 3 != 0:
            column -= 1
            counter += 1
                
        for i in range(0, 3): # 一行に対するボックスは3つごと
            for j in range(0, 3): # ボックス1つにあてはめる数値も3つ
                self.box_array[column + i][counter * 3 + j] = array[i * 3 + j]

    '''
    ゲッター
        ボックスごとにゲットする
        index: ゲットしたい位置の添字
    '''
    def get_array(self, index):
        return self.box_array[index]

    '''
    数独のルールに則って数値が当てはめることができるか確認するメソッド
    ボックスに同じ数値があるかどうか確認
        array: 検証する1次元配列
        column: 何列目に対する検証なのか
        return: 当てはめることができるか否か
    '''
    def available_box_values(self, array, column):
        # 検証列を3の倍数にする
        while column != 0 and column % 3 != 0:
            column -= 1

        for i in range(0, 3): # 一行に対するボックスは3つごと
            for j in array[i * 3:i * 3 + 3]: # [0~2, 3~5, 6~8]ごとに検証するボックスが変わる
                for k in self.box_array[column + i]: # 検証ボックス内の数値を回す
                    if(j == k):
                        return False
        return True

    '''
    配列をリセットする
    '''
    def reset(self):
        self.box_array = [[0 for i in range(1, 10)] for j in range(1, 10)]