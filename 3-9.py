#関数アノテーション
#ドキュメンテーション文字列に加え、 \
#関数の定義部分に引数、戻り値の説明を記述できる

def my_func(n:'この値から足し始める', m:'この値まで足す') -> 'nからmの合計値':
    """nからmまでの合計を返す関数"""
    ret = 0
    for i in range(n, m+1):
        ret += i

    return ret

val = my_func(1, 10)
print(val)