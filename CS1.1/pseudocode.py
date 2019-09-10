fruit_list = ['Apple', 'Brownie', 'Cherry', 'Orange']


def pick_fruits(list, amount):
    new_list = []
    for i in fruit_list:
        new_list.append(fruit_list[amount])

    return print(new_list[amount])


pick_fruits(fruit_list, 2)
