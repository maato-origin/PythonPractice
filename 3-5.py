#内部関数(inner function)とnonlocal宣言

#内部関数(inner function)
def outer_function():
    """外側の関数"""
    print('outer')

    def inner_function():
        """内側の関数"""
        print('inner')

    inner_function()

outer_function()

#関数オブジェクトを使用
def outer_function():
    """外側の関数"""
    print('outer')

    def inner_function():
        """内側の関数"""
        print('inner')

    #内側の関数をオブジェクトとしてreturnする
    f = inner_function
    return f

f = outer_function()
#受け取った内側の関数を実行する
f() #innerが出力される

#nonlocal宣言
def outer_function():
    """外側の関数"""
    x = 100
    print(x)

    def inner_function():
        """内側の関数"""
        nonlocal x
        x = 200
        print(x)

    inner_function()
    print(x)

outer_function()