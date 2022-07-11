a = "1,2,3,4,5,6,7"
print (a.split(","))

numbers = "9,223,332,445,889,775"
separators =","
values = "".join(char if char not in separators else " " for char in numbers).split()
print (values)