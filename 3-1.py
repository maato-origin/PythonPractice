#関数の定義

#z = sample_function(1, 2)  #NameError

def sample_function(x, y):
    z = x + y
    return z

z = sample_function(1, 2)
print(z)

#引数
def sample_function(arg1, arg2):
    print(arg1, arg2)

sample_function('a', 'b')   #順番に引数を指定
sample_function(arg1='c', arg2='d') #キーワードを指定
sample_function(arg2='e', arg1='f') #キーワードの場合は順番通りでなくてよい

#デフォルト引数
def sample_function(arg1, arg2='x', arg3='y'):
    print(arg1, arg2, arg3)

sample_function('a', 'b', 'c')  #引数を全部指定
sample_function('a', arg2='b')  #3番目を省略
sample_function('a')            #2,3番目を省略

#可変長引数
#引数シーケンス
def sample_function(arg1, *arg2):
    print(arg1, arg2)

sample_function('a', 'b', 'c', 'd')

#引数辞書
def sample_function(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)

sample_function('a', 'b', 'c', 'd', key1='x', key2='y', key3='z')

#戻り値
#returnを指定しない場合Noneが返される
def sample_function1():
    """数値を返却"""
    return 1

def sample_function2():
    """何も返さない関数"""
    pass

def sample_function3():
    """複数の値を返却"""
    return 3, 'b'

x = sample_function1()
print(x)
y = sample_function2()
print(y)
a, b = sample_function3()
print(a, b)