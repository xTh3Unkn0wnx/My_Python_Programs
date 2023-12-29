Monday = {'time': [['1:00', '1:30', '2:00', '2:30', '3:00', '3:30'], [True, True, True, True, True, True]], 'name': ['', '', '', '', '', ''], 'email': ['', '', '', '', '', ''], 'topic': ["Office hours", "Office hours", "Office hours", "Office hours", "Office hours", "Office hours"]}
Tuesday = {'time': [['1:00', '1:30', '2:00', '2:30', '3:00', '3:30'], [True, True, True, True, True, True]], 'name': ['', '', '', '', '', ''], 'email': ['', '', '', '', '', ''], 'topic': ["Office hours", "Office hours", "Office hours", "Office hours", "Office hours", "Office hours"]}
Wednesday = {'time': [['1:00', '1:30', '2:00', '2:30', '3:00', '3:30'], [True, True, True, True, True, True]], 'name': ['', '', '', '', '', ''], 'email': ['', '', '', '', '', ''], 'topic': ["Office hours", "Office hours", "Office hours", "Office hours", "Office hours", "Office hours"]}
Thursday = {'time': [['1:00', '1:30', '2:00', '2:30', '3:00', '3:30'], [True, True, True, True, True, True]], 'name': ['', '', '', '', '', ''], 'email': ['', '', '', '', '', ''], 'topic': ["Office hours", "Office hours", "Office hours", "Office hours", "Office hours", "Office hours"]}
schedule = [None, Monday, Tuesday, Wednesday, Thursday]

dayofweek = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']


def schedule_meeting():
    print("\nChoose a day")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    select = int(input(""))
    if select == 1 or select == 2 or select == 3 or select == 4:
        for i in range(0, 6):
            truth = schedule[select]['time'][1][i]
            if truth:
                print(schedule[select]['time'][0][i])
        print("")
        selecttime = input("Enter the time you want to schedule your appointment (e.g. 1:00): ")
        if selecttime in schedule[select]['time'][0] and schedule[select]['time'][1]:
            index = schedule[select]['time'][0].index(selecttime)
            print("Please enter your information")
            tempname = input("Enter your name: ")
            tempemail = input("Enter your email: ")
            temptopic = input("Enter the topic you wanted to discuss (Press enter for default \"office hours\": ") or "office hours"
            schedule[select]['time'][1][int(index)] = False
            schedule[select]['name'][index] = tempname
            schedule[select]['email'][index] = tempemail
            schedule[select]['topic'][index] = temptopic
            print("Your appointment has been made\n")
    else:
        print("Something went wrong, try again\n")


def view_all():
    scheduled = False
    for i in range(1, 5):
        print(f"{dayofweek[i]}: ")
        ind = 0
        for j in schedule[i]['time'][1]:
            if not j:
                temptime = schedule[i]['time'][0][ind]
                tempname = schedule[i]['name'][ind]
                tempemail = schedule[i]['email'][ind]
                temptopic = schedule[i]['topic'][ind]
                print(f"\n{temptime} - {tempname} ({tempemail})")
                print(f"Topic: {temptopic}")
                scheduled = True
            ind += 1
        print("")
    if not scheduled:
        print("\nIt seems you do not have anything scheduled today\n")
    input("If you are done looking, press enter to go back to the menu.")


def menu():
    going = True
    while going:
        print("Main Menu")
        print("Select 1 to create an appointment")
        print("Select 2 to view scheduled appointments")
        print("Select 3 to exit program")
        choice = int(input("Choose what you want to do: "))
        if choice == 1:
            schedule_meeting()
        elif choice == 2:
            view_all()
        elif choice == 3:
            going = False
        else:
            print("Invalid input, try again")


menu()

print("done")