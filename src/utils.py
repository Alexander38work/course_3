# -*- coding: utf-8 -*-

import json
import datetime
def get_data():
    """загрузить данные из файла"""

    with open('data/operations.json', encoding="UTF-8") as file:
        transaction_list = json.load(file)
        return transaction_list


def data_executed(transaction_list):
    """отфильтровать по исполненным платежам и добавить их отдельный    словарь"""
    all_operations = transaction_list
    executed = []
    for operation in all_operations:
        if operation.get('state') == 'EXECUTED':
            executed.append(operation)
    if len (executed) == 0:
        return 'нет исполненных платежей'
    return executed


def sorted_last_five(operations, qty=5):
    """взять заданного количества последних платежей"""
    date_sorted = sorted(operations, key=lambda operation: datetime.datetime.fromisoformat(operation['date']), reverse=True)
    return date_sorted[:qty]


def output_str(sorted5):
    """функция для вывода итогов в консоль"""
    for i in sorted5:
        date = datetime.datetime.fromisoformat(i["date"])
        print (f'{date.strftime('%d.%m.%Y')} {i['description']}\n'
               f'{hidenum(i.get('from', '*'))} -> {hidenum(i.get('to','*'))}\n'
               f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n')




def hidenum (line):
    linesplit = line.split(' ')
    number = linesplit[-1]
    if line.lower().startswith('счет'):
        newnumber = ('**'+number[-4:])
    elif line == '*':
        return "Оплата наличными"
    elif line == '':
        return "некорректный ввод"
    else: newnumber = (number[:4]+' '+number[4:6]+'** **** '+number[-4:])
    linesplit[-1] = newnumber
    return ' '.join(linesplit)
