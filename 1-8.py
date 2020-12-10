#list型　更新操作

#listの要素を更新
l=[1,2,3,4,0]
l[0]=99
print(l)

#listの要素追加
l=[1,2,3]
l.append(4)
print(l)

#リストの要素挿入

#0番目に挿入
l=['a','b','c']
l.insert(0,'x')
print(l)

#2番目に挿入
l.insert(2,'y')
print(l)

#最後尾に挿入
l.insert(-1,'z')
print(l)

#削除

#指定した要素を削除
l=['a','b','c','d','c']

#aを削除
l.remove('a')
print(l)

#重複した値を削除すると先頭側のものが削除される
l.remove('c')
print(l)

#存在しない値を指定するとValuErrorが発生
#l.remove('e')

#指定したインデックスを削除
#del文
l=['a','b','c','d']

del l[2]
print(l)

#先頭の要素を削除
del l[0]
print(l)

#最後の要素を削除
del l[-1]
print(l)

#スライス構文を使った削除
l=['a','b','c','d']
del l[0:2]
print(l)

#pop関数
l=['a','b','c','d']

x=l.pop(2)  #2番目の要素を取り出して削除
print(x)
print(l)