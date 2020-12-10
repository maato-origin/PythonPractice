#lambda式
#一時的に利用する無名関数を記述する方法

func = lambda x: x % 2 == 1

is_odd = func(5)
print(is_odd)   #True

is_odd = func(6)
print(is_odd)   #False

#高階関数
def higher_order(datas, is_target):
    """高階関数のサンプル"""
    for i in datas:
        if is_target(i):
            print(i)

def is_odd(num):
    return num % 2 == 1

datas = [1, 102, 900, 5, 3]
higher_order(datas, is_odd)

def higher_order(datas, is_target):
    """高階関数のサンプル"""
    for i in datas:
        if is_target(i):
            print(i)

def is_multipleof3(num):
    return num % 3 == 0

datas = [1, 102, 900, 5, 3]
higher_order(datas, is_multipleof3)

#lambda式のメリット
def higher_order(datas, is_target):
    """高階関数のサンプル"""
    for i in datas:
        if is_target(i):
            print(i)

datas = [1, 102, 900, 5, 3]
higher_order(datas, lambda x: x % 2 == 1)