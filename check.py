from RPN.calc_rpn import calc_RPN
from RPN.search_rpn_all import search_RPN_all
from quizknock_solver import solver
from sample_input import QUERY


def check_calc_rpn():
    print(f"{calc_RPN('12+')} = {calc_RPN('12+', return_formula=True)}")
    print(f"{calc_RPN('34+12-*')} = {calc_RPN('34+12-*', return_formula=True)}")


def check_search_RPN_all():
    search_RPN_all([1, 2])
    print("\n" + "-"*20)
    search_RPN_all([1, 1])
    print("\n" + "-"*20)
    search_RPN_all([1, 2, 3])


def check_solver():
    print(solver([1, 2, 3, 4], 11))


def solve_sample_puzzle():
    # 各問題を解き、問題番号と式を表示
    for no, input_nums, create_num in QUERY:
        formula = solver(input_nums, create_num)
        print(f"[No.{no}] {formula} = {create_num}")


if __name__ == "__main__":
    print("/// check__calc_rpn function ////")
    check_calc_rpn()
    print("/////////////////////////////////", end="\n\n")

    print("/// check__gen_RPN_all function ////")
    check_search_RPN_all()
    print("/////////////////////////////////", end="\n\n")

    print("/// check__solver function ////")
    check_solver()
    print("/////////////////////////////////", end="\n\n")

    print("/// solve_sample_puzzle function ////")
    solve_sample_puzzle()
    print("/////////////////////////////////", end="\n")
