menu= [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["egg","bread"],
]
for meal in menu:
    if "spam" not in meal:
        print(meal)

        for items in meal:
            print (items)