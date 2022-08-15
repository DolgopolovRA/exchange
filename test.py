# put your python code here
n = int(input())
while n > 10:
    n /= 7
n = int(n)
if n == 1:
    print('понедельник')
elif n == 2:
    print('вторник')
elif n == 3:
    print('среда')
elif n == 4:
    print('четверг')
elif n == 5:
    print('пятница')
elif n == 6:
    print('суббота')
elif n == 7:
    print('воскресенье')