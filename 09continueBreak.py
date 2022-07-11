shopping_list=["milk","pasta","eggs","spam","bread","rice"]



for item in shopping_list:
    if item != "spam":
        print("Buy "+item)

print("----------------------------")

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy "+ item)


print("----------------------------")


shopping_list=["milk","pasta","eggs","spam","bread","rice"]
item_to_find ="spama"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{0} is not found".format(item_to_find))


print ("-----------------------------")

if item_to_find in shopping_list:
    found_at=shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{0} is not found".format(item_to_find))

