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
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?: ")

        read(int(item_index))

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

# Listens to the user input and give them a display for CRUD


def main():
    running = True
    while running:
        selection = user_input(
            "Press" + Fore.RED + " C " + Fore.RESET + "to add to list," + Fore.RED + " R " + Fore.RESET + "to Read from list," + Fore.RED + " P " + Fore.RESET + "to display list, and" + Fore.RED + " Q " + Fore.RESET + "to quit: ")
        running = select(selection)


main()
