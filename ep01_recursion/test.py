def ruler(number_ruler):
    number_ruler -= 1
    count = 0
    while count <= number_ruler:
        print('---', count, '\n-', '\n--', '\n-')
        count += 1
    print(f'--- {number_ruler + 1}')
    return number_ruler


ruler_num = int(input('Input your ruler length >>'))
ruler(ruler_num)
