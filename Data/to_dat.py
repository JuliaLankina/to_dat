import re

char_number = 1002
number_of_files = 16
txt_file_number = 1
exp = '-8'

folder = input("Введите имя папки: ")
#Звезда_80_80

constant_address = 'C:\\Users\\julia\\YandexDisk\\COMSOL\\' + folder + '\\'

file_to_full_array = open(constant_address + folder + '.dat', 'w')
file_to_full_array.write('# name: data' + '\n' + '# type: matrix' + '\n' +
                         '# rows: 256' + '\n' + '# columns: 1 - ' + folder + '\n')

intermediate_array = []
full_array = []

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

    for i in range(0, 16):
        result_list[i] = float(result_list[i])

    intermediate_array = intermediate_array + result_list
    print(result_list)
    txt_file_number = txt_file_number + 1

while number_of_files < len(intermediate_array):
    intermediate_array.pop(number_of_files)
    number_of_files = number_of_files + 16

for r in range(0, (len(intermediate_array) - 16)):
    #print(str(intermediate_array[r]) + '-' + str(intermediate_array[r+16]))
    full_array.append(intermediate_array[r] - intermediate_array[r+16])

for d in range(0, 16):
    #print(str(intermediate_array[d+240]) + '-' + str(intermediate_array[d]))
    full_array.append(intermediate_array[d + 240] - intermediate_array[d])

for add in range(0, len(full_array)):
    full_array[add] = str(full_array[add])
    file_to_full_array.write(full_array[add] + '\n')

print(full_array)