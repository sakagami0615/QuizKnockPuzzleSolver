from RPN.calc_rpn import calc_RPN


def solver(input_nums: list[int | str], create_num: int) -> str|None:
    """
    複数の数値と四則演算を用いて、指定した数値を作成するソルバー

    Args:
        input_nums (list[int | str]): 入力数値リスト(数値は2つ以上)
        create_num (int): 作成する数値

    Returns:
        str|None: 指定した数値を作成できる四則演算式の文字列 (解がない場合はNone)
    """
    n_nums = len(input_nums)    # 入力数値の個数
    n_ops = n_nums - 1          # 演算子の個数
    n_rpn = n_nums + n_ops      # 逆ポーランド記法の文字数

    used = [False] * n_nums     # 使用したinput_numsを記憶する変数

    # DFSにより、あり得る逆ポーランド記法を探索し、create_numと一致する式の場合は、その式(文字列)を返却する
    # rpn: 作成中の逆ポーランド記法
    # n_stack: スタックしている数値の個数
    def dfs(rpn:str = "", n_stack: int = 0) -> str|None:
        nonlocal used

        if len(rpn) >= n_rpn:
            # 生成した逆ポーランド記法の計算を実施
            # create_numと一致した式(文字列)を返却し、一致しない場合はNoneを返却
            if (calc_RPN(rpn) == str(create_num)):
                return calc_RPN(rpn, return_formula=True)
            else:
                return None

        appeared = set()        # 重複防止のために、出現した数値を保存する変数

        for i, num in enumerate(input_nums):
            # 未使用 かつ 未出現の数値の場合、追加可能
            if (not used[i]) and (num not in appeared):
                appeared.add(num)
                used[i] = True
                formula = dfs(rpn + str(num), n_stack + 1)
                # 該当する式が見つかった場合は式を返却
                if formula:
                    return formula
                used[i] = False

        # スタックが2つ以上ある場合は演算子が追加可能
        if n_stack >= 2:
            for op in "+-*/":
                formula = dfs(rpn + op, n_stack - 1)
                # 該当する式が見つかった場合は式を返却
                if formula:
                    return formula

        # create_numと一致する式が見つからない場合はNoneを返却
        return None

    return dfs()
