#bool型

b1=True
b2=False
b3=True

#論理和
b3=b1 or b2
print(b3)

#論理積
b4=b1 and b2
print(b4)

#否定
b5=not b1
print(b5)

b=b1 and b2 and b3
print(b)

b=b1 or b2 and b3
print(b)

#演算子の優先度：not>and>or

#比較演算子とbool型
x=100
y=200
b1=(x<y)
print(b1)

b2=(x>y)
print(b2)

#bool型はint型のサブクラス
b1=True
b2=False

print(int(b1))
print(int(b2))