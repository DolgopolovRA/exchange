# ввод значения N (эту переменную не менять)
N = int(input())

# здесь продолжайте программу
def get_sum(n):
    for i in range(n):
        yield sum(range(1, i+1))


a = get_sum(N)
for _ in range(25):
    print(next(a))

