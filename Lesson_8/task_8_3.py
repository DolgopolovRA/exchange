from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = []
        print(f'name function: {func.__name__}, type of function value: {type(result)}')
        for arg in args:
            result.append(func(arg))
            print(f'{arg}: {type(arg)}', end=', ')
        for _, v in kwargs.items():
            result.append(func(v))
            print(f'{v}: {type(v)}', end=', ')
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


cubs = calc_cube(123)
print(cubs)
