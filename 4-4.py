
#クラスオブジェクト
class Cooridnate:
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
        """座標を表示"""
        print(self.x, self.y)

    def __str__(self):
        """文字列表現を返す"""
        return "({0},{1})".format(self.x, self.y)

#クラスをインスタンス化
cood = Cooridnate() #普通にインスタンスを生成
cood.x = 100 #メンバxに代入
cood.y = 200 #メンバyに代入
cood.show_coordinate()

#クラスをオブジェクトとして扱う
C = Cooridnate #Coordinateクラスのオブジェクトとして変数Cに代入
cood2 = C() #Cからクラスを生成
cood2.x = 300
cood2.y = 600
cood.show_coordinate()

#クラス属性
class MyClass():
    remark = "A"

    def __init__(self):
        self.text = "sample text"

c1 = MyClass()
c2 = MyClass()

#クラス変数にアクセス
print(c1.remark, c2.remark, MyClass.remark) #A A A

#クラス変数を変更
MyClass.remark = "B"
print(c1.remark, c2.remark, MyClass.remark) #B B B