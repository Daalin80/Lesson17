def cels(in_t):
    return 'Температура по Кельвину: ' + str(round(in_t + 273.15, 2)) + \
           ' Температура по Фарренгейту: ' + str(round((in_t * 1.8 + 32), 2))


def kelv(in_t):
    return 'Tемпература по Цельсию: ' + str(round(in_t - 273.15, 2)) + \
           ' Температура по Фарренгейту: ' + str(round((in_t * 1.8 - 459.67), 2))


def farren(in_t):
    return 'Температура по Кельвину: ' + str(round((in_t + 459.67)/1.8, 2)) + \
           ' Tемпература по Цельсию: ' + str(round((in_t - 32)/1.8, 2))


def main():
    in_t = int(input('ТЕМПЕРАТУРА: '))
    in_t_type = input('ТИП (C,K или F): ')
    if in_t_type == 'C':
        cels(in_t)
    elif in_t_type == 'K':
        kelv(in_t)
    elif in_t_type == 'F':
        farren(in_t)
    else:
        print('Ошибка ввода!!!')


if '__name__' == '__main__':
    main()