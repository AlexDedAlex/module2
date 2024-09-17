my_list = [42, 69, 13, 322, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
print(my_list)
while count < len(my_list):
    number = my_list[count]
    count = count + 1
    if number == 0:
        continue
    elif number < 0:
            break
    elif count == len(my_list):
        print(number)
    else:
        print(number)

