#デフォルト引数の破壊
#以下、破壊的な操作
def sample(x, arg=[]):
    arg.append(x)
    return arg

print(sample(1))
print(sample(2))
print(sample(3))

#対策・・・デフォルト引数にはイミュータブルなものを使用する
def sample(x, arg=None):
    if arg is None:
        arg = []
    
    arg.append(x)
    return arg

print(sample(1))
print(sample(2))
print(sample(3))