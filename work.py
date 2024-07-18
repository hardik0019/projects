# #1
# x=10
# print(x)
# #2

# a=5
# b=7.5
# c="hello"
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# #3
# x=25
# y=float(x)
# print(type(y))
# #4
# s="123.45"
# h=float(s)
# print(type(h))
# #5
# a="hello"
# b="world"
# x=a+" "+b
# print(x)
# #6
# s= "python programming"
# print(s[7:18])

# #7
# a=15
# b=4
# print(a*b)
# print(a/b)
# print(a+b)
# print(a-b)
# print(a%b)
# #8
# a=10
# b=20
# print(a<b)
# #9
# x=True
# y=False
# print(x and y)
# print(x or y)
# print(not(x))
# #10
# #11
# #12
# #13
# #14

# #15
# f=45.67
# i=int(f)
# print(i)

# # str= "hello, Hardik,how, are you "
# # print(str.upper())
# # print(str.lower())
# # print(str.strip())
# # print(str.replace(" ","gupta"))
# # print(str.split(","))
# #*-----------------------------------------------------------------------------------*

# string="hello,my,name,is hardik"
# print(string.upper())
# print(string.lower())
# print(string.strip())
# print(string.replace("hello","how"))
# print(string.split(","))
 
# ## formatting the string

# name = "virat"
# str= "hello"
# print(f"hey {str} nice to meet you {name}")

# n1=10
# n2=20

# print(f"the sum of {n1} and {n2} is {(n1+n2):.3f}")
# #------------------------------------------------------------------------------#

# ## escape characters

# str= "john wick"
# print("my name is \"john wick\"")

# #-----------------------------------------------------------------------------#

# str= "hardik gupta"

# print(str.capitalize())
# print(str.count("h"))

# a=10
# b=2
# print(a//b)

# #--------------------------------------------------------------------------------------------#

# #1
# s1 = "hardik"
# s2 = "gupta"

# print(s1+s2)

# #2
# num1 = 10
# num2 = 20
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)

# #3
# str="world cup ended on 25th"
# print(str.isnumeric())

# #4
# vowels=("aeiouAEIOU")
# str="hi my name is hardik nice to meet you"
# print(str.count("a,e,i,o,u"))
# #?


    
    

# #6
# #?

# #7
# str= "The world cup was Great to watch"
# print(str.upper())
# print(str.lower())

# #8
# #?

# #9
# str="my name is hardik"
# substr="hardik"
# print(str.endswith("hardik"))

# #10
# #?

# #-------------------------------------------------------------------------------#
# #1
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(mylist)   
# print(len(mylist))
# print(max(mylist))
# print(min(mylist))
# mylist.append(11)
# print(mylist)
# mylist.remove(8)
# print(mylist)
# mylist.insert(5,8)
# print(mylist)

# #2
# sqlist = [x**2 for x in mylist]
# print(mylist)
# print(sqlist)

# newlist = [x for x in mylist if x%2 == 0]
# print(newlist)

# #3
# reversed = mylist[ : : -1]
# print(reversed)

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = mylist[1: :2]
# print(list2)

# #4
# tuple1 = ("apple", "banana", "cherry")
# print(tuple1)
# print(len(tuple1))
# tuple2 = list(tuple1)
# print(tuple2)
# list3 = tuple(tuple2)
# print(list3)

# #7
# myset = {1, 2, 3, 4, 5}
# print(myset)
# myset.add(6)
# print(myset)
# myset.remove(6)
# print(myset)
# set1 = {"hello","hardik",1, 4, 7}
# set2 = ["infinity","sorry",2, 8, 5]
# set3 = set1.union(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)
# set5 = set1.difference(set2)
# print(set5)

# #5
# mytuple = (2, 5, 7, 9)
# (red, pink, blue, green) = mytuple
# print(red)
# print(pink)
# print(blue)
# print(green)

# #8
# set1 = {1, 2, 3, 5, 6}
# newset = {x**2 for x in set1}
# print(newset)
# list1 = [2, 4,  6, 8]
# print(list1)
# unqlist = set(list1)
# print(unqlist)

# list3 = list(unqlist)
# print(list3)

# #9
# num1 = 10
# num2 = 20
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num2%num1)

# #10
# a = 5
# b = 10
# print(a==b)
# print(a>=b)
# c = 8
# print(a<= c <=b)

# #11
# val1 = 10
# val2 = 20
# val3 = 30
# print(val1==val2==val3 and val1!=val2!=val3)
# print(val1==val2==val3 or val1!=val2!=val3)
# print(not(val1!=val2!=val3))

#-------------------------------------------------------------------------#

# list = [1, 2, 3, 4, 5, 9, 8, 6, 7]
# list.sort (reverse=True)

#1
# n = int(input("the number is:"))

# if n%2==0:
#     print("it is even")
# else:
#     print("it is odd")

#2
# n = int(input("the number is:"))
# if n%3==0:
#     print("fizz")
# elif n%5==0:
#     print("buzz")
# elif n%3==0 and n%5==0:
#     print("fizzbuzz")
# else:
#     print("none")

#3
n = int(input("the number is:"))

for i in range(2, int(n**0.5) + 1):
    if n%i==0:
        print(i)







