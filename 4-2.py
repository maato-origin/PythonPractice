
#クラスの基本

#クラスの構成要素
class Coordinate:
    """座標クラス"""

    def __init__(self):
        """初期化"""
        self.x = 0
        self.y = 0

    def move(self, x, y):
        """平行移動"""
        self.x += x
        self.y += y

    def show_coordinate(self):
        """座標の表示"""
        print(self.x, self.y)

    def __str__(self):
        """文字列表現を返す"""
        return "({0}, {1})".format(self.x, self.y)

#クラスの利用サンプル
cood = Coordinate() #インスタンスの生成
cood.x = 100 #メンバxに代入
cood.y = 200 #メンバyに代入
cood.show_coordinate()  #メソッドの利用

print(cood) #文字列表現を取得する