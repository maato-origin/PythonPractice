
#ファイル操作の基本
print('ファイル操作の基本\n')

print('ファイルの読み込み\n')
f = open('sample.txt', 'r') #ファイルを開く
text = f.read() #ファイルを読み込む
print(text) #テキストファイルの内容が出力される
f.close()   #ファイルを閉じる

print('ファイルの書き込み\n')
f = open('sample.txt', 'w')
f.write('aaaa bbbb cccc')
f.close()

#追記したい場合
#f = open('sample2.txt', 'a')

#読み書きしたい場合
#f = open('sample2.txt', 'r+')

#文字コードの指定(sjisを使いたい例)
#f = open('sample.txt', 'r', encoding='shift_jis')

#closeとwith文
print('closeとwith文\n')

with open('sample.txt', 'r') as f:
    text = f.read()
    print(text)