
#クラスの継承
class Base:
    def func1(self):
        print('func1')

class Sub(Base):
    def func2(self):
        print('func2')

obj = Sub()
obj.func1()
obj.func2()

#親クラスのメソッドの呼び出し
print('\n親クラスのメソッドの呼び出し')

class Base:
    def func1(self):
        print('func1')

class Sub(Base):
    def func2(self):
        super().func1() #親クラスのメソッドを呼び出し
        print('func2')

obj = Sub()
obj.func2()

#オーバーライド
print('\nオーバーライド')

class Base:
    def func1(self):
        print('func1')

class Sub(Base):
    def func1(self):    #親クラスのメソッドをオーバーライド
        print('sub func2')

obj = Sub()
obj.func1()

#多重継承
print('\n多重継承')

class Base1:
    def func1(self):
        print('func1')

class Base2:
    def func2(self):
        print('func2')

class Sub(Base1, Base2):
    def func(self):
        super().func1()
        super().func2()

obj = Sub()
obj.func()