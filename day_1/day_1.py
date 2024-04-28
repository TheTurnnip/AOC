
word_list = []

with open("./day_1/input.txt") as file:
    for line in file.readlines():
        word_list.append(line)

total = 0

for word in word_list:
    start = 0
    end = len(word) - 1
    
    first_number = None
    first_number_found = False
    last_number = None
    last_number_found = False

    for index in range(len(word)):

        if word[start].isnumeric() and not first_number_found:
            first_number = word[start]
            first_number_found = True

        if word[end].isnumeric() and not last_number_found:
            last_number = word[end]
            last_number_found = True

        start += 1
        end -= 1
    
    total += (int((first_number + last_number)))
    print("\n\n---------------------------------")
    print("Calibration number for word:")
    print("---------------------------------")
    print(first_number + last_number)
    print("---------------------------------")


print("\n---------------------------------")
print("Final Result")
print("---------------------------------")
print(total)