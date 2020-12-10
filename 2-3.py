#for文

#listのfor文
datas = ['a', 'b', 'c']

for v in datas:
    print(v)

#rangeのfor文
for v in range(1, 5, 2):
    print(v)

#dictionaryのfor文
#keyのループ
dic = {'key1':110, 'key2':270, 'key3':350}

for key in dic:
    print(key, dic[key])

#valueのループ
for value in dic.values():
    print(value)

#keyとvalueのループ
for key, value in dic.items():
    print(key, value)

#ループインデックスを取得
#リスト
l = ['a', 'b', 'c']
for i, value in enumerate(l):
    print(i, value)

for i, (key, value) in enumerate(dic.items()):
    print(i, key, value)

#辞書
dic = {'key1':110, 'key2':270, 'key3':350}

for i, key in enumerate(dic):
    print(i, key)

for i, value in enumerate(dic.values()):
    print(i, value)

for i, (key, value) in enumerate(dic.items()):
    print(i, key, value)

#for-else
data_list = ['t', 'e', 's', 't']

for data in data_list:
    print(data)
else:
    print('ループ処理が終わりました')

#break
data_list = [1, 2, 3]
for data in data_list:
    print(data)
    if data > 1:
        break
else:
    print('ループ処理が終了しました')