# -*- coding: utf-8 -*-

from utils import get_data, data_executed, sorted_last_five, output_str


transaction_list = get_data() #ситаем файл json со списком операций
operations = data_executed(transaction_list) #Фильтруем по статусу executed и помещаем исполненные в отдельный список
sorted5 = sorted_last_five(operations) #формируем список из 5 последнийх операций
output_str(sorted5) #выводим итоги