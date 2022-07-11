locations ={
    0:"you are sitting in fromt of computer learning python",
    1:"you are standing at the end of road before a small brick building",
    2:"you are at the top of hill",
    3:"you are inside teh building, a well house for a small street",
    4:"you are in a valley beside stream",
    5:"you are in the forest"
}
exits =[
    {"Q":0},
    {"W":2,"E":3,"N":5,"S":4,"Q":0},
    {"N":5,"Q":0},
    {"W":1,"Q":0},
    {"N":1,"W":2,"Q":0},
    {"W":1,"S":1,"Q":0}
]

loc=1

while True:
    # availableExits=""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    availableExits = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc==0:
        break

    direction = input ("Available exits are " + availableExits).upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in this direction")