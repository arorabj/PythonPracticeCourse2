sampleDict = {"name": "Raj",
              "age": "31",
              "gender" : "M" ,
              "Date_of_birth": "01/01/2001"
        }

while True:
    dict_key = input("please enter the keys:")
    if dict_key == "quit":
        break
    if dict_key not in sampleDict and dict_key=="address":
        sampleDict["address"] = "Delhi, India"
    value = sampleDict.get(dict_key,  "Key not present for" + dict_key)
    print ("Value is "+ value)

for keys in sampleDict:
    print (keys)
    print (sampleDict[keys])



# value assign
sampleDict["address"] = "Delhi, India"

print (sampleDict)


# dict are by deafult unordered
for i in range(10):
    for i in sampleDict:
        print (i + " - " + sampleDict[i])
    print ("-"*40)

#get all keys
print (sampleDict.keys())


#get all items
print (sampleDict.ite   ms())
sampleDict_tuple= tuple(sampleDict.items())
for i in sampleDict_tuple:
    k , v = i
    print (k +' - '+ v)

print (dict(sampleDict_tuple))

# sorting Keys
ordered_keys = list(sampleDict.keys())
ordered_keys.sort()
print ("-"*40)
print ("-"*40)
for i in ordered_keys:
    print (i + " - " + sampleDict[i])


