from functools import wraps


def val_checker(_lambda):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            try:
                if not _lambda(num):
                    raise ValueError()
                res = func(num)
                return res
            except ValueError:
                print(f'wrong value: {num}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(int(input('Введите число: '))))
