#dictionary型のループ処理

#キーのループ
dic = {'key1':110, 'key2':270, 'key3':350}
for key in dic:
    print(key)
    print(dic[key])

#値のループ
for value in dic.values():
    print(value)

#キーと値のループ
for key, value in dic.items():
    print(key, value)