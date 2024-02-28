import pytest

# ファイル保存した関数およびデータの準備
from sample_input import QUERY
from quizknock_solver import solver


# solverで求めた式から値を計算し、指定した値が作成できてるかをテスト
@pytest.mark.parametrize("no, input_nums, create_num", QUERY)
def test_solver(no, input_nums, create_num):
    # 解となる数式を求める(Noneは解なしとなります)
    formula = solver(input_nums, create_num)
    # 解なしの場合はNG
    assert formula != None

    # 求めた数式を実際に計算する
    result = eval(formula)
    # 計算結果と指定した値が一致しない場合NG
    assert result == create_num
