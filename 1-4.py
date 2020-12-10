import math
from decimal import Decimal
from fractions import Fraction

#指数関数
val=math.exp(2)
print(val)

#対数関数
val=math.log(5)
print(val)

#三角関数
val=math.sin(math.pi/2)
print(val)

#Decimalモジュール
x=0.1*3
print(x)

is_equal=(0.1*33==3.3)
print(is_equal)

x=Decimal('0.1')
print(x)
print(x*3)

Decimal('0.3')
is_equal=(x*33==Decimal('3.3'))
print(is_equal)

#fractionモジュール

#分数の定義
x=Fraction(3,7)
print(x)

#約分の確認
y=x*7
print(y)

#小数との演算
z=x+0.1
print(z)