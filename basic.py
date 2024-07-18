# number = "7"
# num = int(number)
# print(type(num))

# a = "hello world!"

# print(len(a))

# a=5
# b=5
# print(a+b)
# #arithmetic operators
# print(a**b) 
# print(b//a)


# #comparison operators
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# #logical operators
# print(a==b and a!=b)
# print(a==b or a!=b)
# print(not(a!=b))

# a = "hello dost kaise ho!"
# print("dost" in a)

# a=3
# b=4
# c=5
# d=10
# mylist = [3,4,5,10]
# print(mylist[2])

# for i in mylist:
#     print(i)


# #-----------------------------------------------------------------------------------#
#     # str= "hello, Hardik,how, are you "
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

# #----------------------------------------------------------------------------------#

# #list python

# a=2
# b=3
# c=4

# d = [2, 3, 4, "true", "hardik", "false"]
# print(len(d))

# e = (3, 5, 6, 8, 9)
# f=list(e)
# print(type(e))

# a=(1, 2, 3, 4, 5)
# b=list(a)
# print(type(b))

# d = [2, 3, 4, "true", "hardik", "false"]
 
# print(d[-1])

# print("true" in d)

# d[2] = "10"
# print(d)

# d[2:5]=["gupta", "cricket", "9"]
# print(d)

# list = [2, 3, 4, 5]
# list.append(9)

# print(list)

# list.insert(1, 7)
# print(list)

# list2=[8, 9, 10]

# print(list+list2)

# list2.remove(9)
# print(list2)

# list2.pop(1)
# print(list2)

# list2.clear()
# print(list2)

# e=[]

# d = [2, 3, 4, 1, 9, 8]
# for i in d:
#     if i>3:
#       e.append(i)
#       print(i)

# print(e)

# d = [2, 3, 4, 1, 9, 8]
# e = [i for i in d if i>3] #list comprehension
# print(e)

# list = [5, 8, 7, 9, 4, 3]
# list.sort(reverse=True)
# print(list)

# list2 = ["apple", "banana", "mango"]

# list2.sort()
# print(list2)

# list2 = ["apple", "banana", "mango"]
# list2.copy()
# print(list2)


# #-----------------------------------------------------------------------#
# #tuple

# mytuple = (3, 4, 5, 6, 3, 4, 8, 2)
# print(len(mytuple))


# set= {1, 3, 5, 8, 5, 2, 9}
# print(set)

# mytuple = (1, 2, 3,(4, 5, 6),(6, 7, 8,(9, 10, 11)))
# for i in mytuple[4][3]:
#     print(i)

# #to check if number is even or odd
# a = 4
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# #dictionary

# mydict = {
#     "name": "audi",
#     "model": "a4",
#     "color": "red",
# }

# print(mydict["name"])
# person = dict(name="virat", age=25, passion="cricket")
# print(person)

# print(person.keys())
# print(person.values())

# person["debut"] = 2009
# print(person)
# print(person.items())

# for i in person:
#     print(f'{i} - > {person[i]}')

# for x,y in person.items():
#     print(f"{x} -> {y}")


# mydict = {
#     "child1":{
#         "name": "child1",
#         "age" : 5,

#     },
#     "child2" :{
#         "name": "child2",
#         "age" : "6",
#     }
# }

# print(mydict["child2"]["age"])

# for i,j in mydict.items():
#     print(f"{i} ->{j}")
#     for x,y in j.items():
#         print(f"{x} ->{y}")

# #----------------------------------------------------------------------------------#

#n = int(input("enter any number-"))

# if n%2==0:
#     if n%3==0:
#         print("it is perfect number")

# else:
#     print("wrong number")

# if n%2==0 or n%3==0:
#     print("it is perfect number")
# else:
#     print("not perfect")

# a = int(input("enter any number A:"))
# b = int(input("enter any number B:"))
# c = int(input("enter any number C:"))

# if a<b and a<c:
#     print("A is smallest")
# elif b<c and b<a:
#     print("b is smallest")
# else:
#     print("c is smallest")


# if n%2==0:
#     print("good")
# elif n%3==0:
#     print("great")
# elif n%5==0 and n%2==0:
#     print("perfect")
# else:
#     print("bad")

# list = [1, 2, 3, 8, 6, 7]
# list.sort (reverse=True)

# list2 = [1, 2, 3, 4, 5, 6]
# list2.sort(reverse = True)
# print(list2)
# print(list2[1])

# n = int(input("enter any number-"))
# if n<=0:
#     print("invalid")
# elif n==1:
#     print("not prime")
# elif n==2:
#     print("prime number")
# elif n%2==0:
#     print("not prime")
# else:
#     for i in range(1,n):
#         if n%i ==0:
#             continue
#         else:
#             print("prime number")

#         print("not a prime number")
        
# n = int(input("enter any number-"))
# s = 0
# for i in range(n+1):
#     s += i
# print(s)

# functions

# def greet():
#     print("good morning")
# def greet_night():
#     print("good night!")

# greet()
# greet_night()

# def greet(s, a):
#     print(f"good {s} and {a}!!")

# greet("man", "hello")

# n = int(input("the number is:"))

# list = [25, 60, 50, 40]
# def numbers(list):
#     print(sum(list))
     
# numbers(list)
    
# n = int(input("the number is:"))

# def number(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")

# number(n)


# class fruits:
#     name = "apple"
#     color = "red"

#     def newfruit(self):
#         return f'{self.name}, {self.color}'


# obj = fruits()
# print(obj.name)
# print(obj.name)
# print(obj.newfruit())

# class animal:
 
#      def __init__(self,name,age):
#          self.name = name
#          self.age = age
   
#      def makesound(self):
#         print("sound of animal")


# class fruit(animal):
#     def makesound(self):
#         print("mango", 45)

# obj = fruit("apple", 20)
    
    
# obj.makesound()
# print(obj.age)



# from python import animal

# obj = animal("elephant", 47)
        