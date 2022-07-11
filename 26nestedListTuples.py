sampleList = [("egg","spam","bread"),
              ("egg","spam","butter"),
              ("bread", "spam", "butter"),
              ("bread", "jam", "butter")
              ]

for item in sampleList:
    item1,item2,item3 =item
    print (item1,item2,item3)

print ()

for item1, item2, item3 in sampleList:
    print (item1,item2,item3)


