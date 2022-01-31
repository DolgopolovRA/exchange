import itertools

# with open('bakery.csv', 'a', encoding='utf-8') as f:
#     f.write(f'{input("Price: ")}\n'.zfill(9))
with open('bakery.csv', 'r', encoding='utf-8') as rf:
    res = itertools.islice(rf, 0, 10)
    # print(*res, sep='')
    print(tuple(res))
