from colorama import Fore, Back, Style

print("Checklist:")

checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    print(checklist[index])


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(Fore.CYAN + str(index) + Fore.RESET + " " + list_item)
        index += 1

# Checks to see if it was completed and marks it as completed


def mark_completed(index):
    checklist[index] = Fore.GREEN + '√' + Fore.RESET + checklist[index]

# Gets the user input


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def select(function_code):
    # Add to the checklist
    if function_code.lower() == "c":
        input_item = user_input("Input item: ")
        create(input_item)
    # Read from the checklist
    elif function_code.lower() == "r":
        item_index = user_input("Index Number?: ")
        # Checks for invalid input
        if int(item_index) >= len(checklist):
            print(Fore.RED + 'Invalid input' + Fore.RESET)
        else:
            read(int(item_index))
    # List items in the checklist
    elif function_code.lower() == "p":
        list_all_items()
    # Removes an item from the checklist
    elif function_code.lower() == "d":
        destroy_item = user_input('What index do you want to remove?: ')

        if int(destroy_item) >= len(checklist):
            print(Fore.RED + 'Invalid input' + Fore.RESET)
        else:
            destroy(int(destroy_item))
            print('Removed index: ' + Fore.GREEN + destroy_item + Fore.RESET)
    # Updates an item from the checklist
    elif function_code.lower() == "u":
        get_index = user_input('What index do you want to update?: ')

        if int(get_index) >= len(checklist):
            print(Fore.RED + 'Invalid input' + Fore.RESET)
        else:
            update_item = user_input(
                'Update item ' + Fore.YELLOW + get_index + Fore.RESET + ' to: ')
            update(int(get_index), update_item)
    # Quit the checklist
    elif function_code.lower() == "q":
        return False
    else:
        print("Unknown Option")
    return True


def test():
    print('Testing now!')

    # Creates a checklist
    create('Remember to clean dishes')
    create('Pay apartments bills')
    list_all_items()

    # Updates the 2nd item on the checklist
    update(1, 'Pay apartments bills')
    list_all_items()

    # Testing delete functionality
    destroy(0)
    list_all_items()
    # Testing specific select functions
    create('Testing')

    select('d')
    select('r')
    select('q')

    read(0)


test()

# Listens to the user input and give them a display

# def main():
#     running = True
#     while running:
#         selection = user_input(
#             "Press" + Fore.RED + " C " + Fore.RESET + "to add to list," + Fore.RED +
#             " R " + Fore.RESET + "to Read from list," + Fore.RED + " P " + Fore.RESET + "to display list" + Fore.RESET + Fore.RED + " D " +
#             Fore.RESET + "to remove an item" + Fore.RED + " U " + Fore.RESET + "to update an item, and" + Fore.RED + " Q " + Fore.RESET + "to quit: ")
#         running = select(selection)


# main()
