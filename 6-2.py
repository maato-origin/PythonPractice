import os
import shutil

#ファイル/ディレクトリの存在チェック
print('ファイル/ディレクトリの存在チェック\n')

path = 'sample.py'

if os.path.exists(path):
    print('指定したパスは存在する')

    if os.path.isfile(path):
        print('ファイルです')
    if os.path.isdir(path):
        print('ディレクトリです')
else:
    print('指定したパスは存在しません')

#ファイル/ディレクトリの作成と削除
#ファイルの削除
print('\nファイルの削除\n')
#os.remove('file1.txt') #なければエラーになる

#ディレクトリの作成
print('\nディレクトリの作成\n')

os.mkdir('dir_1')
os.makedirs('dir_2/dir_3')

#ディレクトリの削除
os.rmdir('dir_1')
os.removedirs('dir_2/dir_3')

#ファイル/ディレクトリの移動とコピー
#shutil.copy('sample.txt', 'sample2.txt')    #単一コピー
#shutil.copytree('dir_1/', 'dir_2/') #ディレクトリごと再帰的にコピー
#なければエラー