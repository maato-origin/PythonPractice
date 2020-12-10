#none型

#noneの判定
val=None
if val is None:
    print('val is None')

#noneの評価と空文字
if val:
    print('True')
else:
    print('False')

val=''

if val:
    print('True')
else:
    print('False')

#noneの文字列表現
var=None
print(var)