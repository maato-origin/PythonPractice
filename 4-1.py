
#classを定義
class User(object):
    """
    ユーザークラス
    """

    def __init__(self, name, age):
        """
        初期化
        :param name:名前
        :param age: 年齢
        """
        self.name = name
        self.age = age

def say(user):
    """指定した内容であいさつする"""
    print('私の名前は%sです。%s歳です。' % (user.name, user.age))

#user1を生成
user1 = User("suzuki", 26)
#user2を生成
user2 = User("sato", 31)

#user1の名前と年齢を出力
say(user1)
#user2の名前と年齢を出力
say(user2)

#classを定義（メソッドもまとめる）
class User2(object):
    """
    ユーザークラス
    """

    def __init__(self, name, age):
        """
        初期化
        :param name:名前
        :param age: 年齢
        """
        self.name = name
        self.age = age

    def say(self):
        """指定した内容であいさつ"""
        print('私の名前は%sです。%s歳です。' % (self.name, self.age))

#user3を生成
user3 = User2("tanaka", 27)
#user4を生成
user4 = User2("yamada", 25)

#user3の名前と年齢を出力
user3.say()
#user4の名前と年齢を出力
user4.say()