number = "7"
num = int(number)
print(type(num))

a = "hello world!"

print(len(a))

a=5
b=5
print(a+b)
#arithmetic operators
print(a**b) 
print(b//a)


#comparison operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operators
print(a==b and a!=b)
print(a==b or a!=b)
print(not(a!=b))

a = "hello dost kaise ho!"
print("dost" in a)

a=3
b=4
c=5
d=10
mylist = [3,4,5,10]
print(mylist[2])

for i in mylist:
    print(i)


#-----------------------------------------------------------------------------------#
    # str= "hello, Hardik,how, are you "
# print(str.upper())
# print(str.lower())
# print(str.strip())
# print(str.replace(" ","gupta"))
# print(str.split(","))
#*-----------------------------------------------------------------------------------*

string="hello,my,name,is hardik"
print(string.upper())
print(string.lower())
print(string.strip())
print(string.replace("hello","how"))
print(string.split(","))
 
## formatting the string

name = "virat"
str= "hello"
print(f"hey {str} nice to meet you {name}")

n1=10
n2=20

print(f"the sum of {n1} and {n2} is {(n1+n2):.3f}")
#------------------------------------------------------------------------------#

## escape characters

str= "john wick"
print("my name is \"john wick\"")

#-----------------------------------------------------------------------------#

str= "hardik gupta"

print(str.capitalize())
print(str.count("h"))

a=10
b=2
print(a//b)

#--------------------------------------------------------------------------------#

