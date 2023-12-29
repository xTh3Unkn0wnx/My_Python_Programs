import re

# Simulated log data
# Don't change this!

users = set()
useritem = dict()


def print_user(mylist):
    for user, action, item in mylist:
        if action == "AddToCart" and user not in users:
            users.add(user)
            useritem[user] = set()
            useritem[user].add(item)
        elif action == "AddToCart":
            if item not in useritem[user]:
                useritem[user].add(item)

    for i in users:
        print(f"{i} added the followings items to cart: {', '.join(useritem[i])}")


def valid_log_data(data):
    pattern = r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s(\w+)\s(\w+):(\w+)?"
    found = re.findall(pattern, data)
    return found


log_data = """
2023-05-10 10:15:30 User123 Login
2023-05-10 10:17:45 User123 ViewItem:Item456
2023-05-10 10:20:10 User123 AddToCart:Item456
2023-05-10 10:25:20 User123 Logout
2023-05-10 11:15:30 User456 Login
2023-05-10 11:17:45 User456 ViewItem:Item789
2023-05-10 11:20:10 User456 AddToCart:Item789
2023-05-10 11:25:20 User456 Logout
2023-05-10 12:15:30 User789 Login
2023-05-10 12:17:45 User789 ViewItem:Item123
2023-05-10 12:25:20 User789 Logout
2023-05-10 13:15:30 User101112 Login
2023-05-10 13:17:45 User101112 ViewItem:Item456
2023-05-10 13:20:10 User101112 AddToCart:Item456
2023-05-10 13:25:20 User101112 Logout
2023-05-10 14:15:30 User131415 Login
2023-05-10 14:17:45 User131415 ViewItem:Item789
2023-05-10 14:25:20 User131415 Logout
2023-05-11 10:15:30 User123 Login
2023-05-11 10:17:45 User123 ViewItem:Item111
2023-05-11 10:20:10 User123 AddToCart:Item111
2023-05-11 10:25:20 User123 Logout
2023-05-12 10:15:30 User123 Login
2023-05-12 10:17:45 User123 ViewItem:Item111
2023-05-12 10:20:10 User123 AddToCart:Item111
2023-05-12 10:25:20 User123 Logout
User999 ViewItem:Item456
User999 AddToCart:Item456
"""

newlist = valid_log_data(log_data)

print_user(newlist)
