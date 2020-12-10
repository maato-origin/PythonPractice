#シーケンス型共通演算

#包括判定
list_data=['a','b','c','d']

#含まれているかどうかを判定
b1='a' in list_data
print(b1)

b2='x' in list_data
print(b2)

#含まれていないかどうかを判定
b3='a' not in list_data
print(b3)

b4='x' not in list_data
print(b4)

#結合
list_data1=['a','b','c']
list_data2=['d','e','f']

#リストの結合
new_list=list_data1+list_data2
print(new_list)

#結合の繰り返し
new_list=list_data1*3
print(new_list)

#スライス文
text="ABCDEFG"

#0番目から2番目の手前まで
print(text[0:2])

#開始インデックス省略
print(text[:2])

#2番目から最後まで
print(text[2:7])

#最後を省略
print(text[2:])

#1つ飛ばし
print(text[0:7:2])

#要素数
#リスト
l=[1,2,3]
print(len(l))

#タプル
t=('a','b','c','d')
print(len(t))

#文字列
s="abcdefg"
print(len(s))

#最初に出現するインデックス
l=['a','b','c','d']
print(l.index('c'))
#print(l.index('x')) #ValueError

text="abcefg"
print(text.index('b'))
print(text.index('ef'))
#print(text.index('x')) #ValueError

#出現する回数
text="abcefg abcdefg"
print(text.count('b'))
print(text.count('ef'))
print(text.count('x'))