a="The no. is odd"
b="The no. even"

try:
    for i in range(1,100):
        if (i%2 == 0):
            print("after first for loop :" + b)
            for i in range (1,3):
                print("after second for loop :" + b)
        else:
            print(a)
    print("*" * 80)
except :
    print ("Error is ")
finally:
    print("execute final piece of code ")

