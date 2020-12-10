#while文
is_conti = True

while is_conti:
    print('キーを入力してください')
    c = input()

    if c == 'end':
        is_conti = False
    else:
        print(c + 'が入力されました')

#while-else
is_conti = input()
while is_conti:
    print('キーを入力してください')
    c = input()

    if c == 'end':
        is_conti = False
    else:
        print(c + 'が入力されました')
else:
    print('処理を終了します')

#break文
is_conti = input()
while is_conti:
    print('キーを入力してください')
    c = input()

    if c == 'end':
        break
    else:
        print(c + 'が入力されました')
else:
    print('処理を終了します')   #breakするとここは呼び出されない