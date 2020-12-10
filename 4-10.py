
#ディスクリプタ
print('\nディスクリプタ')

class MyDescriptor:
    """ディスクリプタクラス"""

    def __init__(self, text):
        self.text = text

    def __get__(self, instance, owner):
        return "* " + self.text

    def __set__(self, instance, text):
        self.text = text + "!"

    def __delete__(self, instance):
        del self.text
        print('text属性が削除された')

class Sample:
    """属性にディスクリプタを持つ"""
    descriptor = MyDescriptor('sample')

obj = Sample()
print(obj.descriptor)   # * sample

obj.descriptor = 'sample2'
print(obj.descriptor)   # * sample2!

del obj.descriptor  #text属性が削除された
#print(obj.descriptor)   #AttributeError