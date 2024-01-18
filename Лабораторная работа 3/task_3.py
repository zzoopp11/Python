# TODO  Напишите функцию count_letters

def count_letters(text):
    original_list = list(main_str)  # Преобразуем исходную строку в список символов
    sort_list = []

    for element in original_list:  # Сортируем список, исключая все символы кроме букв
        if element.isalpha():
            element = element.lower()
            sort_list.append(element)  # На выходе получаем список букв с нижним регистром

    list_letters = list(set(sort_list))
    list_letters.sort()  # Список букв (сортированный)

    list_numbers_letters = []

    for element in list_letters:  # Создаем список кол-ва каждой буквы в тексте
        sum = sort_list.count(element)
        list_numbers_letters.append(sum)

    # Из двух списков сделаем словарь - буква: ee кол-во в тексте
    dict_numbers_letters = dict(zip(list_letters, list_numbers_letters))

    return dict_numbers_letters

# TODO Напишите функцию calculate_frequenc

def calculate_frequenc (the_dict):

    sum_letters = 0
    for key in the_dict:  # Считаем общее кол-во букв
        sum_letters = sum_letters + the_dict.get(key)

    for key in the_dict:  # Заменяем значение кол-ва букв на частоту
        frequency = the_dict.get(key) / sum_letters
        frequency_round = round(frequency, 2)
        the_dict[key] = frequency_round

    return the_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

dict_of_numbers = count_letters(main_str)
dict_of_frequenc = calculate_frequenc(dict_of_numbers)

for key, count in dict_of_frequenc.items():
    print(key, ":", count)
