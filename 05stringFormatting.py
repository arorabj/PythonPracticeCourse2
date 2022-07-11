for i in range(1,13):
    print ("No. is {0} squared is {1} cube is {2}".format(i, i ** 2, i**3))

print()
# right alignment
for i in range(1,13):
    print ("No. is {0:2} squared is {1:3} cube is {2:4}".format(i, i ** 2, i**3))

print()
# left alignment
for i in range(1,13):
    print ("No. is {0:2} squared is {1:<3} cube is {2:<4}".format(i, i ** 2, i**3))


pi = 22/7
print ("pi is : {0}".format(pi) )
print ("pi is : {0:12}".format(pi) )
print ("pi is : {0:12f}".format(pi) ) # by deafult f gives 6 decumal points
print ("pi is : {0:12.50f}".format(pi) ) # .<number>f will give that many decimal points max allowed are 51 to 53 in python
print ("pi is : {0:52.50f}".format(pi) )
print ("pi is : {0:62.50f}".format(pi) )
print ("pi is : {0:72.50f}".format(pi) )
print ("pi is : {0:<72.50f}".format(pi) )



#another way to format string is

print (f"pi is {pi}")
print (f"pi is {pi:12.53f}")