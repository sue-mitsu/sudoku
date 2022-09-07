'''
列ごとの2次元配列を持つクラス
'''
class Column():
    # 列ごとの配列
    column_array = [[]]

    '''
    コンストラクタ
    配列の初期化
    '''
    def __init__(self):
        # 9 * 9の配列を全て0で埋める
        self.column_array = [[0 for i in range(1, 10)] for j in range(1, 10)]

    '''
    セッター
    添字を指定して列ごとにセットする
        array: セットする1次元配列
        index: セットしたい位置の添字
    '''
    def set_array(self, array, index):
        for array_index in range(0, 9):
            self.column_array[array_index][index] = array[array_index]

    '''
    ゲッター
    列ごとにゲットする
        index: ゲットしたい位置の添字
    '''
    def get_array(self, index):
        return self.column_array[index]

    '''
    数独のルールに則って数値が当てはめることができるか確認するメソッド
    列に同じ数値があるかどうか確認
        array: 検証する1次元配列
        return: 当てはめることができるか否か
    '''
    def available_column_values(self, array):
        for array_index in range(0, 9): # arrayを回す
            for column_value in self.column_array[array_index]:
                if array[array_index] == column_value:
                    return False
        return True

    '''
    配列をリセットするメソッド
    '''
    def reset(self):
        self.column_array = [[0 for i in range(1, 10)] for j in range(1, 10)]
        