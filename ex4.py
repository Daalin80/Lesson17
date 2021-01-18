import re

def format_phone(num):
    pattern = r'\b[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})\b'
    match = re.findall(pattern, num)
    try:
       (d1, d2, d3, d4) = re.findall(pattern, num)[0]
       return '(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4
    except IndexError:
        return 'Failed to recognize number'

def main():
    any_num = input('Введите номер телефона: ')
    print(format_phone(any_num))


if '__name__'=='__main__':
    main()