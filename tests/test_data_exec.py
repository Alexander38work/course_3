# -*- coding: utf-8 -*-
import pytest
import os
from src.utils import data_executed, get_data

def test_executed():
    """тест, который проверяет статус операции в выборке executed"""
    transaction_list = get_data()  # ситаем файл json со списком операций
    operations = data_executed(transaction_list)
    for i in operations:
        assert i ['state'] == 'EXECUTED'

def test_executed2():
    '''если список пустой'''
    executed = []
    data_executed(executed)
    assert data_executed(executed) == 'нет исполненных платежей'
