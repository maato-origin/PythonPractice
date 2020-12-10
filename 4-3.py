
#外部からのメンバ追加
class Sample:

    def __init__(self):
        self.x = 100

obj = Sample()
obj.y = 200 #Sample型に変数を追加できる
print(obj.y)

del obj.x #変数を削除することもできる
#print(obj.x) #削除したメンバを参照しようとしたのでエラーが出る

#空のクラスにあれこれ
class Sample: pass #空のクラス

obj = Sample() #空のクラスをインスタンス化
obj.x = 100
obj.y = 200

print(obj.x, obj.y) #100 200

obj2 = Sample()
#print(obj2.x, obj2.y) #メンバを追加したのはobjインスタンス内であるためエラーになる