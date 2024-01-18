
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants (str_1, str_2, separator=',' ):

    set_1 = set(str_1.split(separator))  # Преобразуем строки (выкидываем разделители)
    list_2 = str_2.split(separator)
    set_common = {}  # Объявляем список общих участников

    set_common = set_1.intersection(list_2)

    return set_common

set_common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')

sort_set = sorted(set_common_participants)  # Сортируем список в алфавитном порядке

print(sort_set)  # Печатаем отсортированный список

