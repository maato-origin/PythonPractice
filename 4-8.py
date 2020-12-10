
#プライベートメンバ
print("\nプライベートメンバ")

class Sample():
    def __init__(self):
        self.a = 0
        self._b = 0
        self.__c = 0
        self.__d_ = 0
        self.__e__ = 0

obj = Sample()
a = obj.a   #アクセス可能
b = obj._b  #アクセス可能
#c = obj.__c #AttributeError
#d = obj.__d_ #AttributeError
e = obj.__e__   #アクセス可能