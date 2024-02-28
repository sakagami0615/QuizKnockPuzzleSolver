# 有理数の計算をサポートするライブラリ
# 計算結果が分数になった際、除算による計算誤差が発生してしまうため、このライブラリを使用して対応します。
# 詳細は下記リンクを確認してください。
# https://docs.python.org/ja/3/library/fractions.html
from fractions import Fraction


def calc_RPN_simple(rpn: str) -> Fraction:
    """逆ポーランド記法の演算を実施する

    Args:
        rpn (str): 逆ポーランド記法 (「34+」や「34+12-*」などの文字列)

    Returns:
        Fraction: 演算結果
    """
    def ope(a, b, op):
        match op:
            case "+": return a + b
            case "-": return a - b
            case "*": return a * b
            case "/": return a / b

    ops = "+-*/"
    stack = []

    for i, c in enumerate(rpn):
        # 数値(演算子ではない)の場合、スタックに格納
        if c not in ops:
            stack.append(Fraction(int(c), 1))
        # 演算子の場合は、スタックから数値を2つ取り出して演算する
        else:
            var1 = stack.pop()
            var2 = stack.pop()

            # 計算を実施し、結果をスタックに格納
            result = ope(var2, var1, c)
            stack.append(result)

    # 計算結果を返却
    return stack[0]
