i=0
while i<10 :
    print ("is is now {0}".format(i))
    i += 1


available_exits=["north","south","east","west"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit=input("Please choose a direction :")
    if chosen_exit=="Quit":
        print("Game Over")
        break

print ("glad that you are able to exit")