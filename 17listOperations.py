

shopping_cart =[]
current_choice="-"

# append opertaion
while current_choice != "0":

    if current_choice in "123456":
        print ("Adding item {} to shopping cart".format(current_choice))
        if current_choice=="1":
            shopping_cart.append("Computer")

        elif current_choice=="2":
            shopping_cart.append("Monitor")

        elif current_choice=="3":
            shopping_cart.append("Mouse")

        elif current_choice=="4":
            shopping_cart.append("CPU")

        elif current_choice=="5":
            shopping_cart.append("Mouse mat")

        elif current_choice=="6":
            shopping_cart.append("Hdmi")
    else:
        print ("please add items from list below")
        print("1: Computer")
        print("2: Monitor")
        print("3: Mouse")
        print("4: CPU")
        print("5: Mouse mat")
        print("6: Hdmi")

    current_choice=input()

print (shopping_cart)
print ("Ended")
print ("-"*800)

# iterationg over list
available_parts =["Computer",
                  "Monitor",
                  "Mouse",
                  "CPU",
                  "Mouse mat",
                  "Hdmi"]

shopping_cart =[]
current_choice="-"

while current_choice != "0":

    if current_choice in "123456":
        print ("Adding item {} to shopping cart".format(current_choice))
        if current_choice=="1":
            shopping_cart.append("Computer")

        elif current_choice=="2":
            shopping_cart.append("Monitor")

        elif current_choice=="3":
            shopping_cart.append("Mouse")

        elif current_choice=="4":
            shopping_cart.append("CPU")

        elif current_choice=="5":
            shopping_cart.append("Mouse mat")

        elif current_choice=="6":
            shopping_cart.append("Hdmi")
    else:
        print ("please add items from list below")

        # this for loop is inefficient as python has to look for the index of each element . and whe the list is big it will get slow
        for i in available_parts:
            print ("{0}: {1}".format(available_parts.index(i)+1,i))
    current_choice=input()


print (shopping_cart)
print ("Ended")
print ("-"*800)



# enumerate

# iterationg over list
available_parts =["Computer",
                  "Monitor",
                  "Mouse",
                  "CPU",
                  "Mouse mat",
                  "Hdmi"]

shopping_cart =[]
current_choice="-"

while current_choice != "0":

    if current_choice in "123456":
        print ("Adding item {} to shopping cart".format(current_choice))
        if current_choice=="1":
            shopping_cart.append("Computer")

        elif current_choice=="2":
            shopping_cart.append("Monitor")

        elif current_choice=="3":
            shopping_cart.append("Mouse")

        elif current_choice=="4":
            shopping_cart.append("CPU")

        elif current_choice=="5":
            shopping_cart.append("Mouse mat")

        elif current_choice=="6":
            shopping_cart.append("Hdmi")
    else:
        print ("please add items from list below")

        # this for loop is more efficient
        for number, parts in enumerate(available_parts):
            print ("{0}: {1}".format(number+1,parts))
    current_choice=input()


print (shopping_cart)
print ("Ended")
print ("-"*800)




