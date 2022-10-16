list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_number = list_numbers[0]
max_pos = 0
for i in range(len(list_numbers)):
    if max_number< list_numbers[i]:
        max_number=list_numbers[i]
        max_pos = i

list_numbers[max_pos], list_numbers[-1] = list_numbers[-1], list_numbers[max_pos]



print(list_numbers)
