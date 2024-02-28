from fractions import Fraction


def calc_RPN(rpn: str, return_formula: bool=False) -> Fraction|float|str:
    """逆ポーランド記法の演算を実施する

    Args:
        rpn (str): 逆ポーランド記法
        return_formula (bool): Trueの場合は計算結果、Falseの場合は四則演算式の文字列を返却 (Default: False)

    Returns:
        Fraction|float|str: 演算結果(ゼロ割があった場合はfloat("inf")) or 四則演算式の文字列
    """
    def ope(a, b, op):
        match op:
            case "+": return a + b
            case "-": return a - b
            case "*": return a * b
            case "/": return a / b if b != 0 else float("INF")
            case _:
                raise ValueError(f"op(char) is invalid value (value: {op})")

    ops = "+-*/"
    stack = []
    for i, c in enumerate(rpn):
        # 数値(演算子ではない)の場合、スタック
        if c not in ops:
            stack.append(Fraction(int(c), 1))
        # 演算子の場合は、スタックから数値を2つ取り出して演算する
        else:
            # 演算子に対して、数値が不足している場合は例外を出す
            if len(stack) < 2:
                raise ValueError(f"There is an error in reverse polish notation (notation: {rpn}, index: {i}, char: {c})")

            var1 = stack.pop()
            var2 = stack.pop()

            # 式文字列を返却するときの処理
            if return_formula:
                result = f"{var2} {c} {var1}"
                if i < len(rpn) - 1:
                    result = f"({result})"
                stack.append(result)
            # 計算結果を返却するときの処理
            else:
                result = ope(var2, var1, c)
                # 演算結果が無限(ゼロ割)の場合、無限を返却
                if result == float("inf"):
                    return float("inf")
                stack.append(result)

    # 数値に対して、演算子が不足している場合は例外を出す
    if len(stack) > 1:
        raise ValueError("Insufficient number of operators in reverse polish notation")

    # 計算結果 もしくは 数式を返却
    return stack[0] if return_formula else str(stack[0])
