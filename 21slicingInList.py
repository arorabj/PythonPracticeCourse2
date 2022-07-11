computer_parts =["CPU","Mouse","Keyboard","Monitor","UPS"]

print (computer_parts)

# incorrect way of replacing element in list
computer_parts[3:]="trackpad"
print (computer_parts)


# correct way of replacing element in list
computer_parts [3:]=["trackpad"]
print (computer_parts)


#deleteing item from list
data = [1,2,100,200,300,500,700,900,901,902,903,904,905,906,907,101,102,103,104,106,109]
print(len(data))
del data[0:2]
print (data)

del data[12:]
print (data)

#deleteing item from list
data = [1,2,100,200,300,500,700,900,901,902,903,904,905,906,907,101,102,103,104,106,109]
min_valid = 100
max_valid = 200

for index,value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        print (value)
        print(index)
        del data[index]


print (data)
