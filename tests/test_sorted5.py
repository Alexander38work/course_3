# -*- coding: utf-8 -*-
import pytest
from src.utils import data_executed, get_data, sorted_last_five

def test_sortedlast5():
    """тест, который проверяет что записей действительно необходимое количество"""
    transaction_list = get_data()  # ситаем файл json со списком операций
    operations = data_executed(transaction_list)
    sorted_list5 = sorted_last_five(operations)
    sorted_list10 = sorted_last_five(operations,10)
    assert len(sorted_list5) == 5
    assert len(sorted_list10) == 10

def test_sorted():
    """проверка сортировки по последней дате"""
    transaction_list = get_data()  # ситаем файл json со списком операций
    operations = data_executed(transaction_list)
    sorted_list5 = sorted_last_five(operations)
    assert sorted_list5[-1]['date'] == '2019-11-05T12:04:13.781725'
    assert sorted_list5[-3]['date'] == '2019-11-19T09:22:25.899614'