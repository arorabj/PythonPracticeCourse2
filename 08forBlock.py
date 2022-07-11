parrot="Norwegian Blue"

for characters in parrot:
    print(characters)

numbers="9,223;372:036 854,755;807"
separators =""

for char in numbers:
    if not char.isnumeric():
        seprators = separators + char

separators =numbers[1::4]
print(separators)

values= "".join(char if char not in separators else " " for char in numbers ).split()
print (values)
print([int(val) for val in values])


# range

for i in range(10):
    print (i)

for i in range(0,10):
    print (i)

# define step in range
for i in range(0, 10, 2):
    print(i)


# define negative step in range
for i in range(10 , 0, -2):
    print(i)

#nested loop
for i in range (1,13):
    for j in range (1,13):
        print ("{0} times {1} is {2}".format(i,j,i*j))
    print("-----------------------------")

