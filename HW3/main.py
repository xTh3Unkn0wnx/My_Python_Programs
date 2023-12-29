files = set()


def start_list():
    filename = input("Enter your name: ")
    if filename not in files:
        files.add(filename)
        with open(filename, "w") as f:
            print("Enter items to purchase, press 'x' to stop.")
            while True:
                inp = input("Item: ")
                if inp == 'x':
                    break
                else:
                    f.write(f"{inp} \n")
        print("List created.")


def add_list():
    filename = input("Enter your name: ")
    if filename in files:
        with open(filename, "r") as f:
            print("Current items:")
            for line in f:
                print("- " + line.strip("\n"))
        with open(filename, "a") as f:
            print("Enter items to purchase, press 'x' to stop.")
            while True:
                inp = input("Item: ")
                if inp == 'x':
                    break
                else:
                    f.write(f"{inp} \n")
        print("Items added to list.")


def print_list():
    filename = input("Enter your name: ")
    if filename in files:
        with open(filename, "r") as f:
            for line in f:
                print("- " + line.strip("\n"))


def menu():
    going = True
    while going:
        print("Main Menu")
        print("1. Start a List")
        print("2. Add to a list")
        print("3. Print a List")
        print("4. Quit")
        choice = int(input("Enter your choice (1-4): "))
        try:
            if choice == 1:
                start_list()
            elif choice == 2:
                add_list()
            elif choice == 3:
                print_list()
            elif choice == 4:
                going = False
            else:
                print("Wrong number!")
        except:
            print("Something went wrong, try again!")


menu()
