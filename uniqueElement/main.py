# Algorithm to find unique (non-repeating) characters from a string

rawString = 'YOUR STRING HERE'
repeatingString = []
unique = []

for char in rawString:
    if rawString.count(char) > 1:
        repeatingString.append(char)

for item in rawString:
    if item not in repeatingString:
        unique.append(item)

print(unique)
