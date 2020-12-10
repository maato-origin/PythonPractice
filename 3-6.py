#ジェネレーター
def sample_generator():
    """ジェネレーター関数"""
    yield 'おはよう'
    yield 'こんにちは'
    yield 'こんばんは'

gen_func = sample_generator()   #ジェネレーターオブジェクトを生成

text = gen_func.__next__()
print(text)

text = gen_func.__next__()
print(text)

text = gen_func.__next__()
print(text)

#ループで書き直す
def sample_generator():
    yield 'おはよう'
    yield 'こんにちは'
    yield 'こんばんは'

gen_func = sample_generator()   #ジェネレーターオブジェクトを生成

for text in gen_func:
    print(text)

#ジェネレーターと無限数列
def fibonacci_generator():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1

gen_func = fibonacci_generator()    #ジェネレーターオブジェクトを生成

for i in range(0, 10):
    #10個取得する
    num = next(gen_func)
    print(num)

#ジェネレーターのメソッド
#send()メソッド
#再開待ちのジェネレーターに対し、値を設定する
#sendメソッドで指定した値はyield式の値として設定される
def sample_generator():
    text = yield 'おはよう'
    yield text
    yield text

gen_func = sample_generator()   #ジェネレーターオブジェクトを生成

text = next(gen_func)
print(text)

text = gen_func.send('こんにちは')
print(text)

text = next(gen_func)
print(text)

#throw()メソッド
#再開待ちのジェネレータオブジェクトに対し、例外を送出

#close()メソッド
#再開待ちのジェネレータオブジェクトを正常終了させる