def search_RPN_all(input_nums: list[int | str]) -> list[str]:
    """入力した数値から逆ポーランド記法を全列挙する

    Args:
        input_nums (list[int | str]): 入力数値リスト(数値は2つ以上)

    Returns:
        list[str]: 全列挙した逆ポーランド記法
    """
    n_nums = len(input_nums)    # 入力数値の個数
    n_ops = n_nums - 1          # 演算子の個数
    n_rpn = n_nums + n_ops      # 逆ポーランド記法の文字数

    used = [False] * n_nums     # 使用したinput_numsを記憶する変数
    rpns = []                   # 生成した逆ポーランド記法を保存する変数

    # DFSにより、あり得る逆ポーランド記法を探索し、rpnsに格納する
    # rpn: 作成中の逆ポーランド記法
    # n_stack: スタックしている数値の個数
    def dfs(rpn="", n_stack=0):
        nonlocal rpns, used

        # 逆ポーランド記法を生成できたらいったん表示する
        if len(rpn) >= n_rpn:
            print(rpn, end=", ")
            return

        appeared = set()        # 重複防止のために、出現した数値を保存する変数

        for i, num in enumerate(input_nums):
            # 未使用 かつ 未出現の数値の場合、追加可能
            if (not used[i]) and (num not in appeared):
                appeared.add(num)
                used[i] = True
                dfs(rpn + str(num), n_stack + 1)
                used[i] = False

        # スタックが2つ以上ある場合は演算子が追加可能
        if n_stack >= 2:
            for op in "+-*/":
                dfs(rpn + op, n_stack - 1)

    dfs()
    return rpns
