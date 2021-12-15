for percent in range(1, 101):
    if 5 <= percent <= 20:
        text_percent = 'процентов'
    elif percent % 10 == 1:
        text_percent = 'процент'
    elif 2 <= percent % 10 <= 4:
        text_percent = 'процента'
    else:
        text_percent = 'процентов'

    print(f'{percent} {text_percent}')
