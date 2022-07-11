a =12
b =3
print (a+b)     # 15
print(a-b)      # 9
print(a*b)      # 36
print(a/b)      # 4.0
print(a//b)     #interger division,rounder down to minus infinity
print(a % b)    #modulo : remainder after interger division
print(a**b)     #a power b

print() #print empty line
# in below code a/b can't be used as it will give the float value and range has to have "int"
for i in range (1, a//b ):
    print (i)

#operator precedence
#PEMDAS (Parenthisis, exponents , multiplication/division, addition/substraction
#BEDMAS (brackets, exponents , division/mulitplication, addition/substraction
#BODMAS (brackets, order , division/mulitplication, addition/substraction
#BIDMAS (brackets, index , division/mulitplication, addition/substraction
print (a + b / 3 - 4 * 12)          #-35.0
print (a + (b / 3) - (4 * 12))      #-35.0
print ((((a + b) / 3) - 4) * 12)    #12.0
print (((a + b) / 3 - 4) * 12)      #12.0

print (a / (b * a )/ a)