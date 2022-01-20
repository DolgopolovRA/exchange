
def get_jokes(n=3, flag=True):
    """
    Generates a set number of jokes

    :param n: number of jokes
    :param flag: allow/prohibit repetition of words

    """

    from random import choice

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    fun = []

    for i in range(n):
        elem = [choice(nouns), choice(adverbs), choice(adjectives)]
        fun.append(' '.join(elem))

        if flag:
            nouns.remove(elem[0])
            adverbs.remove(elem[1])
            adjectives.remove(elem[2])
            if nouns == [] or adverbs == [] or adjectives == []:  # шутки закончились :-)
                break

    return fun


print(get_jokes())
