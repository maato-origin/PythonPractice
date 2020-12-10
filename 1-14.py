#set型の基本

#setの初期化
s={'A','B','C'}
print(s)

#初期化時に重複がある場合
s={'A','B','C','A'}
print(s)

#TypeError unhashable type
#s={'A',[1,2,3]}
#↑はlistがハッシュ化可能でないためエラー
#タプルは利用可能
s={'A',(1,2,3)}
print(s)

#listからsetを生成
l=['a','b','c','d']
s=set(l)
print(s)

#setのイテレーション
data_set={'a','b','c'}
for s in data_set:
    print(s)    #集合の要素が出力される

#setの更新操作
s={1,2,3}
s.add(4)
print(s)    #{1,2,3,4}

#setの要素削除
s={1,2,3,4}
s.remove(4)
print(s)
#s.remove(99) KeyErrorが発生する

s.discard(99)
print(s)

#frozenset イミュータブルなset
fs=frozenset(['a','b','c'])
print(fs)