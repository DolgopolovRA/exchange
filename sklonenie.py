for procent in range(1, 101):
    #if 5 <= procent <= 20:
    #    text_procent = 'процентов'
    if procent % 10 == 1:
        text_procent = 'процент'
    elif 2 <= procent % 10 <= 4:
        text_procent = 'процента'
    else:
        text_procent = 'процентов'

    print(f'{procent} {text_procent}')
    # коммент
