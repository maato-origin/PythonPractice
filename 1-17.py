#イミュータブルオブジェクトとid関数

#id関数
num=100
text="aaaa"
dic={'key':200}

print(id(num))
print(id(text))
print(id(dic))

text1="aaa"
text2=text1
text3=text1+'bbb'

print(id(text1))
print(id(text2))
print(id(text3))

text1="bbb"
print(id(text1))