first = input('Введите целое число: ')
second = input('Введите целое число: ')
third = input('Введите целое число: ')
if first == second == third:
    print(3)
if first == second or second == third or first == third:
    print(2)
if first != second and second != third and first !=third:
    print(0)

