# -*- coding: utf-8 -*-
from src.utils import hidenum

def test_hidenum1 ():
    """тест проверяющий функцию маркирования"""
    assert hidenum("Счет 64686473678894779589") == "Счет **9589"

def test_hidenum2():
    assert hidenum("Счет 88947715234") == "Счет **5234"

def test_hidenum3():
    assert hidenum("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_hidenum4():
    assert hidenum("Visa 8990922113665229") == "Visa 8990 92** **** 5229"

def test_hidenum5():
    assert hidenum("") == "некорректный ввод"

def test_hidenum6():
    assert hidenum("*") == "Оплата наличными"