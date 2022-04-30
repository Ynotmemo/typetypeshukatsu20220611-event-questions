def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    left_index = 0
    right_index = len(array) - 1
    while True:
        # 先頭からの探索
        # 必ず基準値が最初のスワップ対象に選ばれる
        while array[left_index] < pivot:
            left_index += 1

        # 末尾からの探索
        while array[right_index] >= pivot:
            right_index -= 1

            #　配列の要素が全てが基準値以上と確認できたら終了
            if right_index == 0:
                break

        # 探索未完了 -> スワップ後，探索最下位
        # 探索完了 -> 分割語のそれぞれで再帰的にソートを行う
        if left_index < right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
        else:
            return sort(array[: right_index+1]) + sort(array[right_index+1: ])

if __name__ == '__main__':
    main()
