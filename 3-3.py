#global宣言

#グローバル変数とローカル変数
x = 100
def sample_function():
    print(x)

sample_function()

#グローバル変数の更新
x = 100
def sample_function():
    x = 200
    print(x)

sample_function()   #関数内部でxの値を変更し、それを出力
print(x)    #100が出力される。関数の外側の値は変更されていない

x = 100
def sample_fucntion():
    global x #global宣言 xはglobal変数であることを明示する
    x = 200
    print(x)

sample_function()   #関数内部でxの値を変更
print(x)            #関数の外側の値が変更されている