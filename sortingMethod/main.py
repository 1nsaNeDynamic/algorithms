# Sorting algorithm, Sorts data in form on a list (integer/float, string, boolean) values.

unsortedList = [1, 'apple', True, 'banana', 45, 32, 45.7, 'pineapple', 99, False, 'vinegar', 76.4, 'watermelon', 65]

stringChars = []
integerChars = []
boolChars = []
floatChars = []

sortedList = []

for item in unsortedList:
    if type(item) == str:
        stringChars.append(item)
    elif type(item) == int or type(item) == float:
        integerChars.append(item)
    elif type(item) == bool:
        boolChars.append(item)
    
for i in range(1, len(integerChars) + 1):
    minItem = min(integerChars)
    sortedList.append(minItem)
    integerChars.remove(minItem)

for i in range(1, len(stringChars) + 1):
    minItem = min(stringChars)
    sortedList.append(minItem)
    stringChars.remove(minItem)

for i in range(1, len(boolChars) + 1):
    minItem = min(boolChars)
    sortedList.append(minItem)
    boolChars.remove(minItem)


print(sortedList)
