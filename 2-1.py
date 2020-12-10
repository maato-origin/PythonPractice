#関係演算(等価と比較演算)

#等価
x=3
y=3
z=7

b1=(x==y)
b2=(x==z)

print(b1)
print(b2)

#オブジェクトの等価性
x=[1,2]
y=x
z=[1,2]

#IDの確認
print(id(x))
print(id(y))
print(id(z))

#同じ値かどうか判定
b1=(x==y)
b2=(x==z)
print(b1)
print(b2)

#同じオブジェクトかどうかを判定
b3 = (x is y)
b4 = (x is z)
print(b3)
print(b4)

#比較演算子
x = 3
y = 5
z = 7
b1 = (x < y)
print(b1)

b2 = (x < y < z)
print(b2)