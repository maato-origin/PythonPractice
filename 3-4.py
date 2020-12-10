#関数オブジェクト
def sample_function():
    text = 'sample'
    print(text)
    return '戻り値'

text = sample_function()    #通常の呼び出し
print(text)

f = sample_function #関数オブジェクトとして変数fに格納

text = f()  #関数オブジェクトを実行
print(text) #戻り値も取得できる

def param_func():
    return 'sample'

def sample_function(f):
    x = f()
    print(x)

sample_function(param_func)