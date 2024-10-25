# from important1 import good,hello
# from functools import reduce

# while True:
#     try:
#         a = int(input())
#         b = int(input())
#         c = a+b
#     except:
#         print("number adikkadaa ")

#     else:
#         print(c)
#         break   

# good()

# hello()


# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [11,12,13,14,15]
# list3 = ["minhaj","shamsu","dilshad"]

# zipped = list(zip(list1,list2,list3))

# print(zipped)

# zipped = [(1, 11, 'minhaj'), (2, 12, 'shamsu'), (3, 13, 'dilshad')]

# list1 , list2 , name = zip(*zipped)
# print(list1)
# print(list2)
# print(name)


# list1 = [10,21,32,44,20]
# # k = list(map(lambda x:x*2  ,list1))
# # print(k)
# k = reduce(lambda x,y:x+y  , list1)
# print(k)

# class hello:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

# class good(hello):
#     def prin(self):
#         print(f"my name is {self.name}, my age is {self.age}")

# k = hello("minhaj", 18)
# good.prin(k)

# class Example:
#     def say_hello(self):
#         return "hello"
    
# example = Example()
# print(example.say_hello())

# def say_hello_world():
#     return "hello world"

# example.say_hello = say_hello_world
# print(example.say_hello())

# class Greeting:
#     def say_hello(self):
#         return "hello"
    
# greeting = Greeting()
# # print(greeting.say_hello())
# def new_say_hello():
#     return "hello world"

# greeting.say_hello = new_say_hello
# print(greeting.say_hello())
# class Dog:
#     species = "canis lups familiar"


#     @classmethod
#     def get_species(cls):
#         return cls.species
    
# print(Dog.get_species())


# list1 = ["banana", "apple", "orange"]
# list1.insert(2,"cherry")
# print(list1)

# tuple1 = (1,2,3,4,5)
# new_tuple = tuple1 + (6,)
# print(new_tuple)

# list1 = [1,2,3,4,5]
# squered_dict = {num:num**2 for num in list1}
# print(squered_dict)

# old_dict = {1:21,2:32,4:54}
# new_dict = {x:x*2 for x in old_dict  }
# print(new_dict)

# word = "HELLO"
# letter_count = {letter:word.count(letter) for letter in word}
# print(letter_count)


# str = "abc"
# new_dict = {index:{str[i]:i**2} for str[i] in str}

# def decor(func):
#     def inner():
#         result = func()
#         # result.upper()
#         return result.upper()
#     return inner



# @decor
# def hello():
#     return "hello world"

# print(hello())

# while True:
#     try:
#         a = int(input())
#         b = int(input())
#         c = a / b

#     except ZeroDivisionError:
#         print("not substract in zero,just think it")
#     except ValueError:
#         print("invalid value")
#     else:
#         print(c)
#         break
#     finally:
#         print("completed")
        
# class single:
#     def hello(self):
#         print("hello world")

# class jango(single):
#     def hello(self):
#         print("good morning")

# k = jango()
# k.hello()


