# set are unordered
#set contains only unique vlaue


# how to create
farms_animals ={"sheep","cow","hen"}

print(farms_animals)

# another way to create
wild_animals = set(["sheep","cow","hen","loin","tiger"])
print (wild_animals)
for animals in wild_animals:
    print (animals)

wild_animals.add("horse")

print(wild_animals)

# creating emply set
empty_set =set()

# below will create dictionary instead of set
empty2_set={}

empty_set.add(1)

# below will fail as this is dictionary
empty2_set.add(1)

