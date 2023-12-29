transaction = list()


def withdraw(file):
    with open(file, "r") as f:
        lines = f.readlines()
        last_line = lines[-1]
        last_line = last_line.strip("\n")
        values = last_line.split(",")
        checkings = float(values[0])
        checkings = round(checkings, 2)
        savings = float(values[1])
        savings = round(savings, 2)
        f.close()
    print("Current Balance")
    print(f"Checkings: ${checkings:.2f}")
    print(f"Savings: ${savings:.2f}")

    print("Would you like to withdraw from your Checking or Savings account?")
    print("1. Checkings")
    print("2. Savings")
    choice = input("Which account do you choose?: ")
    while True:
        try:
            if int(choice) == 1:
                amount = float(input("Enter amount you would like to withdraw: "))
                amount = round(amount, 2)
                if amount > checkings:
                    print("sorry, you do not have enough funds in your Checking account")
                elif amount < 0:
                    print("Sorry, you insert a negative amount which is not valid")
                else:
                    checkings = checkings - amount
                    with open(file, "a") as f:
                        f.write(f"{checkings:.2f},{savings:.2f}\n")
                        f.close()
                    transaction.append(f"You have withdrawn ${amount:.2f} from your Checking account\n")
                    break
            if int(choice) == 2:
                amount = float(input("Enter amount you would like to withdraw: "))
                amount = round(amount, 2)
                if amount > savings:
                    print("sorry, you do not have enough funds in your Savings account")
                elif amount < 0:
                    print("Sorry, you insert a negative amount which is not valid")
                else:
                    savings = savings - amount
                    with open(file, "a") as f:
                        f.write(f"{checkings:.2f},{savings:.2f}\n")
                        f.close()
                    transaction.append(f"You have withdrawn ${amount:.2f} from your Savings account\n")
                    break
        except ValueError:
            print("You can only input numbers only, try again")
        except TypeError:
            print("You can only input numbers only, try again")
        except:
            print("Something went wrong, try again!")


def deposit(file):
    with open(file, "r") as f:
        lines = f.readlines()
        last_line = lines[-1]
        last_line = last_line.strip("\n")
        values = last_line.split(",")
        checkings = float(values[0])
        checkings = round(checkings, 2)
        savings = float(values[1])
        savings = round(savings, 2)
        f.close()
    print("Current Balance")
    print(f"Checkings: ${checkings:.2f}")
    print(f"Savings: ${savings:.2f}")

    print("Would you like to deposit to your Checking or Savings account?")
    print("1. Checkings")
    print("2. Savings")
    choice = input("Which account do you choose?: ")
    while True:
        try:
            if int(choice) == 1:
                amount = float(input("Enter amount you would like to deposit: "))
                amount = round(amount, 2)
                if amount < 0:
                    print("Sorry, you insert a negative amount which is not valid")
                else:
                    checkings = checkings + amount
                    with open(file, "a") as f:
                        f.write(f"{checkings:.2f},{savings:.2f}\n")
                        f.close()
                    transaction.append(f"You have deposited ${amount:.2f} to your Checking account\n")
                    break
            if int(choice) == 2:
                amount = float(input("Enter amount you would like to deposit: "))
                amount = round(amount, 2)
                if amount < 0:
                    print("Sorry, you insert a negative amount which is not valid")
                else:
                    savings = savings + amount
                    with open(file, "a") as f:
                        f.write(f"{checkings:.2f},{savings:.2f}\n")
                        f.close()
                    transaction.append(f"You have deposited ${amount:.2f} to your Savings account\n")
                    break
        except ValueError:
            print("You can only input numbers only, try again")
        except TypeError:
            print("You can only input numbers only, try again")
        except:
            print("Something went wrong, try again!")


def receipt(name):
    with open("receipt.txt", "w") as f:
        f.write(f"Thank you {name} for your patronage!\n")
        f.write("\n")
        f.write("Here is a list of all transactions you did today\n\n")
        for i in transaction:
            f.write(i)
        with open(name + ".txt", "r") as g:
            lines = g.readlines()
            last_line = lines[-1]
            last_line = last_line.strip("\n")
            values = last_line.split(",")
            checkings = float(values[0])
            savings = float(values[1])
            g.close()
        f.write("\nCurrent Balance\n")
        f.write(f"Checking: ${checkings:.2f}\n")
        f.write(f"Savings: ${savings:.2f}\n")
        f.close()
    with open("receipt.txt", "r") as f:
        lines = f.readlines()
        for j in lines:
            print(j.strip("\n"))
        print("")
        f.close()



def change_pin(name):
    index = 0
    with open("users.txt", "r") as f:
        lines = f.readlines()
        for i, words in enumerate(lines):
            words.strip("\n")
            val = words.split(",")
            if val[0] == name:
                index = i
                break
        f.close()
    while True:
        new_pin = input("Enter new PIN: ")
        confirm = input("Confirm PIN: ")
        if new_pin == confirm and len(new_pin) == 4 and new_pin.isnumeric():
            break
        elif len(new_pin) != 4 or not new_pin.isnumeric():
            print("Your new PIN needs to be 4 numbers")
        else:
            print("PINs did not match, press enter to try again or type \'x\' to exit")
            choice = input()
            if choice == 'x':
                return
    old_line = lines[index]
    old_values = old_line.split(",")
    old_values[1] = new_pin + "\n"
    new_line = ",".join(old_values)
    lines[index] = new_line
    with open("users.txt", "w") as g:
        for i in lines:
            g.write(i)
        g.close()


def user_login():
    name = input("What is your username?: ")
    listed = False
    failed = False
    tries = 3
    try:
        with open("users.txt", "r") as f:
            for line in f:
                info = line.strip("\n")
                info = info.split(",")
                if name == info[0]:
                    listed = True
                    while tries != 0:
                        pw = input("enter password: ")
                        if pw == info[1]:
                            break
                        else:
                            if tries > 1:
                                print("Wrong password")
                            tries = tries - 1
                            if tries == 0:
                                failed = True
            if not listed:
                print("Sorry, user not listed in our records")
            f.close()
    except:
        print("file does not exist")
        f.close()
    if listed and not failed:
        user_menu(name + ".txt", name)
    if failed:
        print("You failed three times!")


def user_menu(file, name):
    filename = file
    while True:
        print("1. Withdraw money")
        print("2. Deposit money")
        print("3. Print receipt")
        print("4. Change PIN")
        print("5. Log out")
        try:
            choose = int(input("Which one you choose?: "))
            if choose == 1:
                withdraw(filename)
            elif choose == 2:
                deposit(filename)
            elif choose == 3:
                receipt(name)
            elif choose == 4:
                change_pin(name)
            elif choose == 5:
                transaction.clear()
                break
            else:
                print("Wrong input, try again!")
        except:
            print("Something went wrong, try again")


def admin_menu():
    tries = 3
    with open("admin.txt", "r") as f:
        line = f.readline()
        val = line.split(",")
        pw = val[1]
        pw = pw.strip("\n")
        f.close()
    while tries > 0:
        password = input("Enter password: ")
        if password == pw:
            tries = 0
            while True:
                new_username = input("Enter new user's username: ")
                while True:
                    new_pw = input("Enter new users password: ")
                    confirm = input("Confirm password: ")
                    if new_pw == confirm and len(new_pw) == 4:
                        with open("users.txt", "a") as f:
                            f.write(f"{new_username},{new_pw}\n")
                            f.close()
                        break
                new_file = new_username+".txt"
                with open(new_file, "w") as f:
                    f. write("checking,savings\n")
                    f.write("500,1000\n")
                    f.close()
                break
        else:
            if tries > 1:
                print("Wrong password, try again")
            tries = tries - 1
            if tries == 0:
                print("You failed three times")


def main_menu():
    while True:
        print("1. Login")
        print("2. Admin: add user")
        print("3. Quit")
        try:
            choice = int(input("Which one you choose?: "))
            if choice == 1:
                user_login()
            elif choice == 2:
                admin_menu()
            elif choice == 3:
                print("Want to hear a roof joke? The first one's on the house.")
                break
            else:
                print("Wrong input, try again")
        except ValueError:
            print("Invalid input, please enter a number")
        except KeyboardInterrupt:
            print("Program interrupted by user")
        except:
            print("Something went wrong, try again")


main_menu()
