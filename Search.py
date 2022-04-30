def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    #　探索範囲の上限(upper)と下限(lower)の初期値を設定
    lower_index = 0
    upper_index = len(sorted_array)-1

    while (upper_index - lower_index) > -1:

        middle_index = (upper_index + lower_index) // 2

        # 探索領域の真ん中の値との比較で探索範囲を更新
        if sorted_array[middle_index] > target_number:
            upper_index = middle_index - 1

        elif sorted_array[middle_index] < target_number:
            lower_index = middle_index + 1

        # 探索対象が存在した場合、そのインデックスを返却
        else:
            return middle_index

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
