
#例外の送出
print('例外の送出\n')

def sample(num):
    if type(num)!=int:
        raise TypeError('パラメータが不正です')

    return num * 10

x = sample(10)
#y = sample(5.5) #TypeErrorが発生する

print(x)

#例外の再送出
print('\n例外の再送出')

x = 1000
y = 2

try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print('除算に0が指定された')
    raise e

#独自例外の礼儀
print('\n独自例外の定義')

class ParamError(Exception):
    pass

def sample(num):
    if type(num) != int:
        raise ParamError('パラメータが不正です')

    return num * 10

x = sample(10)
y = sample(5.5)