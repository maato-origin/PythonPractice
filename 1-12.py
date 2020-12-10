#str(文字列)型
#初期化
text1='シングルクォートで囲む'
text2="ダブルクォートでもOK"

#エスケープシーケンス
text="得意なプログラミング言語は\"C++\"です"
print(text)

#文字列の結合
text1='今日は'
text2='いい天気'
text3=text1+text2
print(text3)

#オブジェクトの文字列表現と文字列結合
num=5
text='text'

print(num)
print(text+str(num))
#print(text+num) #TypeError