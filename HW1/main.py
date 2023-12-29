# Do not change this code
numbers = [2, 3, 7, 8, 9, 10, 11, 12, 13, 16, 18, 20, 21, 24, 25, 27, 28, 30, 31, 32, 35, 39, 43, 44, 45, 47, 48, 51,
           54, 56, 58, 60, 61, 62, 63, 65, 70, 71, 72, 75, 76, 77, 81, 83, 84, 85, 87, 89, 92, 95, 97]


# This is a list of 50 random numbers, sorted ascending
# In the top right of this browser window in replit, click "Fork" and it'll copy this code over to your account
# Start your code below this line

def findmy(numbers1, value, start=0, end=None):
    if end is None:
        end = len(numbers) - 1
    if start > end:
        return -1
    else:
        middle = (start + end) // 2
        if numbers1[middle] == value:
            return middle
        elif numbers1[middle] < value:
            return findmy(numbers1, value, middle + 1, end)
        else:
            return findmy(numbers1, value, start, middle - 1)


inp = int(input("Enter a number: "))

if findmy(numbers, inp) != -1:
    print(f"The number {inp} is in index {findmy(numbers, inp)} of the list")
else:
    print(f"The number {inp} is not found on the list")