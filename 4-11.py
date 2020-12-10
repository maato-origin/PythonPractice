
#クラスデコレータ
print('クラスデコレータ\n')

def add_member(cls):
    """型オブジェクト(クラスオブジェクト)に対し属性を追加"""
    cls.x = 'sample'

    return cls

@add_member
class Sample:
    """何もないクラス"""
    pass

obj = Sample()  #Sampleクラスをインスタンス化
print(obj.x)    #Sampleクラスにない属性xを取得できる