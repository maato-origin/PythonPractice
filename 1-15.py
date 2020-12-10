#set型と集合演算

#Union
s1={'A','B','C'}
s2={'C','D','E'}
s=s1.union(s2)
print(s)
print(s1)

#intersection
s1={'A','B','C'}
s2={'C','D','E'}
s=s1.intersection(s2)
print(s)

#Difference
s1={'A','B','C'}
s2={'C','D','E'}

#s1-s2
s=s1.difference(s2)
print(s)

#s2-s1
s=s2.difference(s1)
print(s)

#包括判定
s1={'A','B'}
s2={'A','B','C'}
s1.issubset(s2)

s1={'A','B','C'}
s2={'A','B'}
s1.issuperset(s2)