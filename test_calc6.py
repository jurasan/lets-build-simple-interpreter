from calc6 import Lexer, Interpreter


def eval_expr(expr):
    lexer = Lexer(expr)
    interpreter = Interpreter(lexer)
    return interpreter.expr()


def test_calc():
    assert eval_expr('3') == 3
    assert eval_expr('2 + 7 * 4') == 30
    assert eval_expr('7 - 8 / 4') == 5
    assert eval_expr('14 + 2 * 3 - 6 / 2') == 17
    assert eval_expr('7 + 3 * (10 / (12 / (3 + 1) - 1))') == 22
    assert eval_expr('7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)') == 10
    assert eval_expr('7 + (((3 + 2)))') == 12
