my_list = [
    [1, None, 2, 3, 4 + 5j, 6],
    [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1],
    ['1','2','3.6',None,'4+5.7j','6']
] # исходный список


int_list = [] # создаем пустой список
float_list = [] # создаем пустой список
str_list = [] # создаем пустой список
for item in my_list: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это три внутренних списка)
    types = [] # создаем пустой список
    for elem in item: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это уже все внутренности трьох внутренних списков)
        el_type = type(elem) # переменной el_type назначаем определить тип данных для элементов, которые выбрали строчкой ранее
        types.append(el_type.__name__) # вместо данных,выводим наименование типа данных; и выводим в список 'types'
    single_types = [] # создаем пустой список
    for i_type in types: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это список с наименованием типа данных)
        if i_type not in single_types: # определяем условие, если вышеуказанный элемент отсутствует в пустом списке 'single_types' то
            single_types.append(i_type) # то закрепить его первым в списке
    types_count = [] # создаем пустой список
    for element_type in single_types: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это список с наименованием типа данных 'single_types')
        type_count = types.count(element_type) # считаем количество типов данных
        types_count.append(type_count) # выводим вышеуказанные данные в список 'types_count'
    max_types_count = max(types_count) # считаем типы данных которые преобладают и присваиваем это переменной 'max_types_count'
    index_max = types_count.index(max(types_count)) # определяем индексы типов данных которые преобладают
    main_type = single_types[index_max] # определяем тип данных который преобладает
    separated_list = [] # создаем пустой список
    for element in item: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это три внутренних списка основного списка)
        if type(element).__name__ == main_type: # определяем условие, если тип данных для элементов в вышеуказанном списке, равняется переменной 'main_type'
            separated_list.append(element) # то выводим такие элементы в данный список

    int_list.extend(separated_list) # выводим в пустой список 'int_list' список 'separated_list'
    float_list.extend(separated_list) # выводим в пустой список 'float_list' список 'separated_list'
    str_list.extend(separated_list) # выводим в пустой список 'str_list' список 'separated_list'

res_int_list = [] # создаем пустой список
for i in int_list: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это список 'int_list')
    if type(i).__name__ == 'int': # создаем условие, если тип данных элементов в вышеуказанном списке является 'int'
        res_int_list.append(i) # то включить такой элемент в список 'res_int_list'
print('res_int_list: ', res_int_list) # выводим окончательный список 'res_int_list'

res_float_list = [] # создаем пустой список
for i in float_list: # циклом "for" определяем элементы, к которым будут применяться циклы (в данном случае это список 'float_list')
    if type(i).__name__ == 'float': # создаем условие, если тип данных элементов в вышеуказанном списке является 'float'
        res_float_list.append(i) # то включить такой элемент в список 'res_float_list'
print('res_float_list: ', res_float_list) # выводим окончательный список 'res_float_list'

res_str_list = [str(i) for i in str_list] # если тип данных элементов в списке 'str_list' является 'str', то включить такой элемент в список 'res_float_list'
print('res_str_list: ', res_str_list) # выводим окончательный список 'res_str_list'
