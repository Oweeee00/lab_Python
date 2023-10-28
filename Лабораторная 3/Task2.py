# TODO Напишите функцию find_common_participants
def find_common_participants(line_1, line_2, x=','):
    int = list(set(line_1.split(x)).intersection(line_2.split(x)))
    int.sort()
    return int


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, x='|'))
