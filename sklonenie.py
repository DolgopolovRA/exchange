for percent in range(1, 101):
    if 11 <= percent <= 14:
        text_percent = 'процентов'
    elif percent % 10 == 1:
        text_percent = 'процент'
    elif 2 <= percent % 10 <= 4:
        text_percent = 'процента'
    else:
        text_percent = 'процентов'

    print(f'{percent} {text_percent}')
