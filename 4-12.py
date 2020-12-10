
#特殊メソッド
print('特殊メソッド\n')

class User():
    """
    ユーザークラス
    """

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def __str__(self):
        return "name:" + self.name + " age:" + str(self.age)

user = User("Kuro", 30)

s = str(user)
print(s)