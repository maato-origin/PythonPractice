import math

#クラスメソッド
class Coordinate:
    def __init__(self):
        """初期化"""
        self.x = 0
        self.y = 0

    def show_coordinate(self):
        """座標を表示"""
        print(self.x, self.y)

    @classmethod
    def create_new_cood(cls, x, y):
        """Coordinateオブジェクトを生成して返す"""
        new_cood = cls()    #Coodinateオブジェクトを生成
        new_cood.x = x  #座標設定
        new_cood.y = y  #座標設定
        return new_cood

cood = Coordinate() #インスタンス生成
cood2 = cood.create_new_cood(10, 20)
cood2.show_coordinate()

#スタティックメソッド
class Coordinate_static:
    """座標クラス"""
    
    def __init__(self):
        """初期化"""
        self.x = 0
        self.y = 0

    def show_coordinate(self):
        """座標を表示"""
        print(self.x, self.y)

    @staticmethod
    def calc_dist(cood1, cood2):
        """座標間の距離を計算"""
        x = cood1.x - cood2.x
        y = cood1.y - cood2.y
        return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))

cood1 = Coordinate_static() #インスタンス生成
cood1.x, cood1.y = 100, 100

cood2 = Coordinate_static() #インスタンス生成
cood2.x, cood2.y = 200, 200

dist = Coordinate_static.calc_dist(cood1, cood2)   #スタティックメソッドを実行
print(dist)