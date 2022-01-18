
def get_jokes(n=3, flag=1):
    from random import choice

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    fun = []

    while i < n:
        """формируем список из случайных элементов и добавляем к результирующему списку"""
        elem = [choice(nouns), choice(adverbs), choice(adjectives)]
        fun.append(' '.join(elem))
        """если установлен флаг уникальности, удаляем элементы из списка, чтобы они не повторялись. Далее проверяем,
           если хотя бы в одном списке закончились слова, прекращаем формирование результирующего списка  
        """
        if flag:
            nouns.remove(elem[0])
            adverbs.remove(elem[1])
            adjectives.remove(elem[2])
            if nouns == [] or adverbs == [] or adjectives == []:  # шутки закончились :-)
                break
        i += 1

    return fun


print(get_jokes())
