computer_parts = ["mouse","keyboard", "monitor","cpu"]
another_list = computer_parts

print (computer_parts)
print (another_list)


print ('computer_parts' + ":"+ str(id(computer_parts)))
print ('another_list' + ":"+  str(id(another_list)))

computer_parts += ["hdmi"]

print (computer_parts)
print (another_list)


print ('computer_parts' + ":"+ str(id(computer_parts)))
print ('another_list' + ":"+  str(id(another_list)))
