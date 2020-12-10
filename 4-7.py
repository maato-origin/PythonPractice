
#__new__()メソッド
print('__new__()メソッド')

class MyClass:
    def __new__(cls):
        print('__new__')
        print(cls)

    def __init__(self):
        print('__init__')

    def __str__(self):
        return 'test'

obj = MyClass()

#イミュータブルクラスの継承と__new__
print('\nイミュータブルクラスの継承と__new__')

class MyStr(str):
    def __new__(cls, text):
        print('__new__')
        return super().__new__(cls, text)

    def __init__(self, text):
        print('__init__')

obj = MyStr("my_str")
print(obj)