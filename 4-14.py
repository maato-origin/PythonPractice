
#変数の方を判定

print('type関数')
class Sample():
    pass

#オブジェクトの生成
s = Sample()

#sオブジェクトの型を取得
s_type = type(s)
print(s_type)

print('\ntype関数とisinstance関数')
class Sample1():
    """適当なクラス"""
    pass

class Sample2(Sample1):
    """Sample1を親とするクラス"""
    pass

obj1 = Sample1()    #Sample1型のオブジェクトを生成
obj2 = Sample2()    #Sample2型のオブジェクトを生成

#Typeを使用した場合、Sample2型はSample1型とみなされない
print(type(obj1) == Sample1)    #True
print(type(obj1) == Sample2)    #False
print(type(obj2) == Sample1)    #False
print(type(obj2) == Sample2)    #True

#isinstanceを使用した場合、Sample2型はSample1型とみなされる
print(isinstance(obj1, Sample1))    #True
print(isinstance(obj1, Sample2))    #False
print(isinstance(obj2, Sample1))    #True
print(isinstance(obj2, Sample2))    #True