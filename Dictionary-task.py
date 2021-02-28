# # Homework № 4
# # Task № 1
# # Данное решение сделал до того как показали решение данной задачи,
# # по этому сделано через input,правда к сожалению принимает только тип "int".
# print('****' * 10)
# print('-Try except-')
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# s = a / b
# try:
#     print(s)
# except TypeError :
#     print('Неверный тип ввода данных!')
# except ZeroDivisionError :
#     print('Деление на "ноль"!')


# # Task № 2
print('****' * 10)
cars = [
    {"brand": "ford", "model": "MusTAng Gt500", "year": 2018},
    {"brand": "ZAZ", "model": "Fortza", "year": 2001},
    {"brand": "VW", "model": "Golf GTI", "year": 1999}
]
cars_sorted_year = sorted(cars, key=lambda k: k['year'])
brand_title = cars_sorted_year[2]['brand'].title()
cars_sorted_year[2]['brand'] = brand_title
model_title = cars_sorted_year[2]['model'].title()
cars_sorted_year[2]['model'] = model_title
modification1 = cars_sorted_year[2]['model'][0:8].title()
modification2 = cars_sorted_year[2]['model'][8:].upper()
modification_result = modification1 + modification2
cars_sorted_year[2]['model'] = modification_result
print(cars_sorted_year)