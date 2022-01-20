def num_translate_adv(num_d):
    list_translate = {'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять'}
    if num_d.istitle():
        print(list_translate.get(num_d.lower()).capitalize())
    else:
        print(list_translate.get(num_d))


num = input('Введите слово для перевода: ')

num_translate_adv(num)
