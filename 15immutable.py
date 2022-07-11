string = "abc"
another_string = string
print (string + ":"+ str(id(string)))
print (another_string + ":"+  str(id(another_string)))

string += "def"
print (string)

print (string + ":"+ str(id(string)))
print (another_string + ":"+  str(id(another_string)))

