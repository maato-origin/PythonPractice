#dictionary型

#初期化
dic={'key1':110,'key2':270,'key3':350}
print(dic)

#値へのアクセス
print(dic['key1'])
#print(dic['hoge']) #KeyError

#getメソッド
dic={'key1':110,'key2':270,'key3':350}
print(dic.get('key1'))
print(dic.get('hoge'))

#値の更新
dic={'key1':110,'key2':270,'key3':350}
dic['key1']=200
print(dic['key1'])

#dict()
dic=dict()
dic['key1']=110
dic['key2']=270
dic['key3']=350

d1={'key1':110,'key2':270,'key3':350}
d2=dict(d1)
print(d2)

#dictionaryの要素数
dic={'key1':110,'key2':270,'key3':350}
print(len(dic))