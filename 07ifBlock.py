name=input("Please Enter Your Name:")
age=int(input("How old are you, {0}?".format(name)))

if age>=18 and age is not None :
    print("you are old enough to vote")
else:
    print("Come back in {0} years".format(18-age))


if age< 18 and age is not None:
    print("Come back in {0} years".format(18 - age))
elif age == 18:
    print("Congrat\'s, you are just 18. This is your first vote")
else:
    print("you are old enough to vote")


#operators = < , >, <=, >=, !=, or, and
# chained operator 65 <= age <=100  (between)
# True, false, Not True, Not False
# and has Higher pecedence than or


day = "Friday"
temprature = 27
raining = False

   #false            and #false         or True
if day == "Saturday" and temprature <27 or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

day = "Friday"
temprature = 27
raining = True

   #false            and #false         or False
if day == "Saturday" and temprature <27 or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

#boolean

if 0:
    print("True")
else:
    print("False")

# if inpur is blank or not
name= input("Please enter your name:")
if name:
    print("True")
else:
    print("False")

name= input("Please enter your name:")
if name != "":
    print("True")
else:
    print("False")



# in and not in
parrot ="Norwegian Blue"
letter = input("Enter a letter :")

if letter in parrot and len(letter)>0:
    print ("{} is in {}".format(letter,parrot))
else:
    print("i dont need that letter")

if letter not in parrot or len(letter) == 0:
    print("i dont need that letter")
else:
    print("{} is in {}".format(letter, parrot))

#casefold

if letter.casefold() in parrot.casefold() and len(letter)>0:
    print ("{} is in {}".format(letter,parrot))
else:
    print("i dont need that letter")