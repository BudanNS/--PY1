def get_count_char(str_):
    str_dict = {}
    str_lower = str.lower(str_)
    str_lower = "".join(str.split(str_lower))
    for letter in str_lower:
        if not letter.isalpha():
            continue
        if letter in str_dict:
            str_dict[letter] += 1
        else:
            str_dict[letter] = 1
    return str_dict
      # TODO посчитать количество каждой буквы в строке в аргументе str_

def get_percent_char(str_dict):
    new_str_dict = {}
    sum_ = 0
    for letter in str_dict:
        sum_ += str_dict[letter]
    for letter in str_dict:
        new_str_dict[letter] = round(str_dict[letter]/sum_ *100,1)
    return new_str_dict



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))