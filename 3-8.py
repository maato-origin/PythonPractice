#関数デコレータ
#関数に対して機能を追加・変更する機能
#元の関数の処理には手が入らない

#関数オブジェクトと高階関数の復習
def deco_func(f):
    
    print('deco_func')

    def new_func():
        print('start')
        val = f()
        print(val)
        print('end')

    print('deco_func')

    return new_func

def my_func():
    """1から10までの合計を返す関数"""
    ret = 0
    for i in range(1, 11):
        ret += i

    return ret

f = my_func #関数オブジェクト
new_func = deco_func(f) #新たに機能を追加した関数オブジェクトを作成する
new_func() #新たに作成した関数を実行

#関数デコレータ
def deco_func(f):

    def new_func():
        print('start')
        val = f()
        print(val)
        print('end')

    return new_func

@deco_func
def my_func():
    """1から10までの合計を返す関数"""
    ret = 0
    for i in range(1, 11):
        ret += i

    return ret

my_func()   #実行するとdeco_funcが適用された関数が実行される

#柔軟な引数
def deco_func(f):

    def new_func(*args, **kwargs):
        print('start')
        val = f(*args, **kwargs)
        print(val)
        print('end')

    return new_func

@deco_func
def my_func(n, m):
    """nからmまでの合計を返す関数"""
    ret = 0
    for i in range(n, m+1):
        ret += i

    return ret

my_func(1, 10)
