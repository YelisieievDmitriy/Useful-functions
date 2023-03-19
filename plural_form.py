"""
Выбор формы существительного в зависимости от числа.

:param number: число, по которому нужно выбрать форму существительного
:param forms: список форм слова в порядке: [1, 2, 5] (для котов: ['кот', 'кота', 'котов'])
:return: строка с правильной формой слова
"""
number = int(input())
forms = ['программист','программиста', 'программистов']
def plural_form(number, forms):
    if number % 10 == 1 and number % 100 != 11:
        form = print(number, forms[0])
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        form = print(number, forms[1])
    else:
        form = print(number, forms[2])
    return form
