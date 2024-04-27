# -*- coding: utf-8 -*-

import json
import datetime
def get_data():
    """загрузить данные из файла"""

    with open('operations.json', encoding="UTF-8") as file:
        question_list = json.load(file)
        return question_list


def data_executed ():
    """отфильтровать по исполненным пладтежам и добавить их отдельный    словарь"""
    all_operations = get_data()
    executed = []
    for operation in all_operations:
        if operation.get ('state') == 'EXECUTED':
            executed.append(operation)
    return executed


def sorted_last_five (operations, qty=5):
    """взять заданного количества последних платежей"""
    date_sorted = sorted(operation, key=lambda operation: datetime.datetime.fromisoformat(operation['date']), reverse=True)
    return date_sorted[:qty]


def output_str():
    """функция для вывода итогов"""
    for i in sorted5:
        date = datetime.datetime.fromisoformat(i["date"])
        print (f'{date.strftime('%d.%m.%Y')} {i['description']}\n'
               f'{hidenum(i.get('from', '*'))} -> {hidenum(i.get('to','*'))}\n'
               f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n')


def hidenum (line):
    linesplit = line.split(' ')
    number = linesplit[-1]
    if line.lower().startswith('счет'):
        newnumber = ('**'+number[-4:-1])
    elif line == '*':
        return "Оплата наличными"
    else: newnumber = (number[:4]+' '+number[4:6]+'** **** '+number[-4:])
    linesplit[-1]=newnumber
    return ' '.join(linesplit)

# -*- coding: utf-8 -*-

operation = data_executed()
sorted5 = sorted_last_five(operation)
print (output_str())