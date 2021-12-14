time_interval = int(input('Введите промежуток времени в секундах: '))
if time_interval < 60:
    print(f'{time_interval} сек')
elif 60 <= time_interval < 3600:
    print(f'{time_interval // 60} мин {time_interval % 60} сек')
elif 3600 <= time_interval < 86400:
    minutes = (time_interval % 3600) // 60
    seconds = (time_interval % 3600) % 60
    print(f'{time_interval // 3600} час {minutes} мин {seconds} сек')
else:
    hours = (time_interval % 86400) // 3600
    minutes = ((time_interval % 86400) % 3600) // 60
    seconds = ((time_interval % 86400) % 3600) % 60
    print(f'{time_interval // 86400} дн {hours} час {minutes} мин {seconds} сек')
