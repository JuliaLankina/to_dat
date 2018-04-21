import re
from openpyxl import Workbook

char_number = 1005
number_of_files = 16
txt_file_number = 1
exp = '-8'

folder_name = 'Однородный'

constant_address = 'C:\\Users\\julia\\Desktop\\COMSOL\\' + folder_name + '\\'
excel_file_address = constant_address + folder_name + '.xlsx'

excel_file = Workbook()
sheet_excel = excel_file.active

while txt_file_number <= number_of_files:

    txt_file_address = constant_address + str(txt_file_number) + '.txt'
    txt_file = open(txt_file_address, 'r')

    add_to_index = -1 + txt_file_number
    txt_file.seek(char_number)
    result_string = txt_file.read()
    result_list = re.split('i', result_string)

    for index in range(0, len(result_list)):
        result_list[index] = result_list[index].strip()
        if index == add_to_index:
            result_list[index] = re.split('-', result_list[index])[0]
            result_list[index] = result_list[index] + exp
        else:
            result_list[index] = re.split('-', result_list[index])[0]

    for ind in range(0, 16):
        result_list[ind] = float(result_list[ind])

    print(result_list)
    sheet_excel.append(result_list)
    excel_file.save(excel_file_address)

    txt_file_number = txt_file_number + 1

excel_file.close()