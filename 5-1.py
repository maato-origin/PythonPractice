
#例外処理
print('例外処理\n')

x = 1000
y = 0

try:
    z = x / y
    print(z)
except ZeroDivisionError:
    print('分母0で割り算をしました')

#例外オブジェクトの利用
print('\n例外オブジェクトの利用')

try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print('除算に0が指定された')
    print(type(e), str(e))

#複数の例外を補足する
print('\n複数の例外を補足')

param = {'x':1000, 'y':0}

try:
    x = param['x']
    y = param['y']
    z = x / y
    print(z)

except KeyError as e:   #辞書に存在しない場合の例外を補足
    print('辞書に必要なデータが存在しません')
except ZeroDivisionError as e:  #0除算を補足
    print('除算に0が指定された')
except: #全ての例外を補足
    print('原因不明のエラー')

#else / finally
print('\nelse / finally')

x = 1000
y = 2

try:
     z = x / y
     print(z)
except ZeroDivisionError as e:
    print('1')
else:
    print('2')
finally:
    print('3')