empty =[]

even =[2,4,6,8]
odd = [1,3,5,7,9]

numbers = odd + even
print (numbers)

sorted_numbers = sorted(numbers)
print (sorted_numbers)

print(numbers)

digits = sorted("432985617")
print(digits)

digits = list("432985617")
print(digits)

# one way to copy the list to other variable and they both are stored at different plance
more_numbers = list(numbers)
print(more_numbers)

# another way to copy list
more_numbers = numbers[:]
print(more_numbers)


# there are 12 ways to copy list in python but we should use copy method
more_numbers = numbers.copy()
print(more_numbers)
# they aren't the same list
print (more_numbers is numbers)

print (more_numbers == numbers)

#Fastest way to copy a list
