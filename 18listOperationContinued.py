# enumerate example

for index, character in enumerate("abcdef"):
    print(index, character)

print ("*" *800)
print ("Example Finish")
print ("*" *800)
# list comprehension

available_parts = ["Computer","Monitor","Mouse","CPU","Mouse mat","Hdmi cable","Dvd drive"]
current_choice = "-"
computer_parts = []

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
while current_choice != "0":

    if current_choice in valid_choices:
        print("Adding item {} to shopping cart".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part not in computer_parts:
            computer_parts.append(chosen_part)
        else:
            print ("item already present")
    else:
        print("please add items from list below")
        # this for loop is more efficient
        for number, parts in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, parts))

    current_choice = input()

print(computer_parts)

print ("*" *800)
print ("Example Finish")
print ("*" *800)

# Remove item from list

available_parts = ["Computer","Monitor","Mouse","CPU","Mouse mat","Hdmi cable","Dvd drive"]
current_choice = "-"
computer_parts = []

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
while current_choice != "0":

    if current_choice in valid_choices:
        print("Adding item {} to shopping cart".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part  in computer_parts:

            print ("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part) # you get error when item doesn't exists
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)

    else:
        print("please add items from list below")
        # this for loop is more efficient
        for number, parts in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, parts))

    current_choice = input()

print(computer_parts)

print ("*" *800)
print ("Example Finish")
print ("*" *800)

# Sorting list and merging 2 list using extend

even =  [2,4,6,8]
odd = [1,3,5,7,9]

# extend
even.extend(odd)
print (even)

print ("*" *800)
print ("Example Extend Finish")
print ("*" *800)

#Sorting
even.sort()
print(even)

print ("*" *800)
print ("Example Sorting Finish")
print ("*" *800)

# sorting reverse
even.sort(reverse=True)
print(even)

print ("*" *800)
print ("Example Reverse Sorting Finish")
print ("*" *800)


# sum of all avlues in list
print(sum(even))
print(min(even))
print(max(even))

print ("*" *800)
print ("Example Sum, Min , Max Finish")
print ("*" *800)
