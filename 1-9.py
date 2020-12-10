#list型順序ソート

#元のlistを変更せずにソートする
#昇順
l1=['d','b','c','a']
l2=sorted(l1)
print(l2)

#ソート順序を逆にする
l1=['d','b','c','a']
l2=sorted(l1,reverse=True)
print(l2)

#大文字、小文字を区別せずにソートする
l1=['bc','ac','bD','AB']
l2=sorted(l1)
print(l2)

l2=sorted(l1, key=str.lower)
print(l2)

#元のlistをソートする
#昇順
l=['d','b','c','a']
l.sort()
print(l)

#ソート順序を逆にする
l=['d','b','c','a']
l.sort(reverse=True)
print(l)

#大文字、小文字を区別せずにソートする
l=['bc','ac','bD','AB']
l.sort(key=str.lower)
print(l)