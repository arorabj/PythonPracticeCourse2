flowers = ["Dafodill","Rose","lavender", "Iris","Sunflower","Lily"]

for flower in flowers:
    print(flower)

separator = " | "
# join method is iterator
output = separator.join(flowers)

print (output)

# but if you add a no. to list , join will fail as it cant join int to list

menu= [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["egg","tomato"],
]
for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))

    print(meal)

