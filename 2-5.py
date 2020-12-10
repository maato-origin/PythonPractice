#リスト内包括表記

#使用しない例
data_list = [5, 3, 7, 4, 10, 9, 6]
new_list = []
for num in data_list:
    new_num = num * 2
    new_list.append(new_num)

print(new_list)

#上記と同じ内容をリスト内包括表記で表す
data_list = [5, 3, 7, 4, 10, 9, 6]
new_list = [num * 2 for num in data_list]
print(new_list)

#if文と組み合わせる（偶数の要素だけ取り出す例）
#リスト内包括表記を未使用
data_list = [5, 3, 7, 4, 10, 9, 6]
new_list = []
for num in data_list:
    if num % 2 == 0:
        new_num = num * 2
        new_list.append(new_num)

print(new_list)

#リスト内包括表記を使用
data_list = [5, 3, 7, 4, 10, 9, 6]
new_list = [num * 2 for num in data_list if num % 2 == 0]
print(new_list)

#辞書で試す
data_dict = {"A":"apple", "B":"banana", "C":"orange"}
new_list = ["---" + key + "---" for key in data_dict]
print(new_list)
new_list = [k + ":" + v for k, v in data_dict.items()]
print(new_list)