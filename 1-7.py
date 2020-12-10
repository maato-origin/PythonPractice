#シーケンス型

#テストの点数
num_list=[97,78,88,76,100,85,72,85,92,75]

#出力
for num in num_list:
    print(num)

#list型の基本と初期化

#数値のリスト
l1=[1,3,5,7,9]

#文字列のリスト
l2=['pen','pineapple','apple','pen']

#型の異なるオブジェクトも入れられる
l3=[1,'pen',l1,l2]

#空のリスト
l4=[]

#list関数による初期化
l1=[1,2,3]
l2=list(l1)

#listの要素を取得
l=[1,2,3,4,5]

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[-1])
print(l[-2])
print(l[-3])
print(l[-4])
print(l[-5])

#スライス構文

#リストの初期化
l=['a','b','c','d','e']

#0番目から0番目
print(l[0:1])

#0番目から1番目
print(l[0:2])

#1番目から3番目
print(l[1:4])

#0番目から最後の一つ手前まで
print(l[0:-1])

#0番目から最後まで
print(l[0:])

#0番目から98番目まで（エラーは起きない）
print(l[0:98])

#listの要素数を確認
l=[1,2,3,4,0]
print(len(l))
print(l[len(l)-1])