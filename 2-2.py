#if文

x = 0
if x == 0:
    print('x = 0')

#else文
x = 1
if x == 0:
    print('x = 0')
else:
    print('x != 0')

#elif文
x = 1
if x == 0:
    print('x = 0')
elif x == 1:
    print('x = 1')
else:
    print('x != 0 and x != 1')

#真偽値の評価
if 1:
    print('True')
else:
    print('False')

if 0:
    print('True')
else:
    print('False')

if 0.0:
    print('True')
else:
    print('False')

if 0.1:
    print('True')
else:
    print('False')

if []:
    print('True')
else:
    print('False')

if ():
    print('True')
else:
    print('False')

if None:
    print('True')
else:
    print('False')

if "":
    print('True')
else:
    print('False')

