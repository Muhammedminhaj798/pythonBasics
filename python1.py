# from functools import reduce
# from importent import difference
# print(__name__)
# x = str(3)
# y = int(3)
# z = float(3)

# print(x,y,z)

# x = "hello world"
# y = 122
# z = 23.31

# print(type(x),type(y),type(z))


# a = 10
# A = "minhaj"

# print(a)

# fruits = ["orange", "apple", "mango","cherry"]
# w,x,y,z = fruits
# print(x)
# print(y)
# print(z)
# print(w)

# x = "python is awesome"

# print(x)

# x = "python"
# y = "is"
# z = "awesome"

# print(x,y,z)
# print(x + y + z)

# x = 'awesomme'
# def value():
#     x = "free"
#     print("python is " + x)
# value()

# x = "global" 

# def value():
#     global x
#     x = "awesome" 
# value()

# print("python is " + x)

# x = range(4)

# print(x)

# print(type(x))


# carrom = {"minhaj","shamsudheen","dilshad","jasim","minhaj"}

# print(carrom)

# string = {"minhaj","shamsudheen","dilshad"}
# numbers = {1,4,2,53,53,542,443,34,2,21}
# boolean = {True,False,True,False}


# print(type(string))
# print(type(numbers))
# print(type(boolean))

# x1 = 3 + 2j
# x2 = 1 + 5j

# result = x1 + x2
# print(result)
# print(x1.real)
# print(x1.imag)

# x = 25
# y = 32

# if x > y:
#     print("x greater than y")
# elif x == y:
#     print("x equal to y")
# else:
#     print("x less than y")

# a = 123
# b = 1231
# print("A") if a > b else print("b is less than a") if a == b else print ("a and b ")

# x = 330
# y = 20
# z = 500

# if x > y and z > x:
#     print("both are condition true")

# x = 40

# if x > 10:
#     print("is above 10")
#     if x > 20:
#         print ("is also above 20")
#     else:
#         print("but not above 20")

# i = 1
# while i <= 6:
#     print(i)
#     i += 1

# i = 1
# while i < 10:
#     i += 1
#     if i >= 4 and i <= 7 :
#         continue
#     print(i)

# i = 0
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i id no long oe")    

# fruits = ["apple", "mango", "jackfruit", "cherry", "lemon"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)

# fruits = ["apple", "banana", "lemon", "mango", "cherry", "orange"]
# for x in fruits:
#     if x == "lemon":
#         continue
#     print(x)
# for x in range(31, 1, -2):
#     print(x)

# for x in range(11):
#     print(x)
# else:
#     print("finally print this ")

# for x in range(30):
#     if x == 13:
#         break
#     print(x)
# else:
#     print("finally finished in loop")

# name = ["minhaj", "shamsu", "dilshad", "jasim", "nasiq"]
# fruits = ["apple", "banana", "orange", "cherry", "lemon"]

# for x in name:
#     for y in fruits:
#         print(x ,":", y )

# x = range(5)
# print(list(x))

# my_list = ["apple", "orange", "mango", "cherry", "kiwi", "lemon", "strawberry", "pinapple"]
# # print(my_list[-5:-1])
# if "strawberry" in my_list:
#     print("Yes this inside the list")

# fruits = ["apple", "mango", "orange"]
# this_tuple = ("lemon", "pineapple", "watermelon")
# fruits.extend(this_tuple)
# print(fruits)

# fruits = ("apple", "mango", "cherry")
# k=list(fruits)
# k.remove("apple")
# print(tuple(k))

# fruits = ["apple", "banana", "orange", "apple", "mango", "banana"]
# i = 0
# while i < 5:
#     print(fruits[i])
#     i += 1

# [print(x) for x in fruits]

# fruits = ["apple", "banana", "orange", "mango", "lemon"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# for x in fruits:
#     if "e" in x:
#         newlist.append(x)
# print(newlist)

# newarray = [x for x in fruits]
# print(newarray)

# newlist = [x for x in range(10) if x < 5]
# k = tuple(newlist)

# print(k)
# newlist = [x if x != "banana" else "kiwi" for x in fruits]
# print(newlist)

# fruits.sort(reverse = True)
# print(fruits)

# def myfunc(n):
#     return abs(n - 50)

# thislist = [10,20,30,40,50,120,210,22,12]
# thislist.sort(key=myfunc)
# print(thislist)

# thislist = ["minhaj", "jasim", "dilshad"]
# mylist = thislist.copy()
# print(mylist,thislist)
# thislist = ["appple", "orange", "banana", "grapes"]
# newlist = list(thislist)
# print(newlist)

# join1 = ["mijnahj", "jasim", "dishad"]
# join2 = [1,2,3]

# join1.extend(join2)
# print(join1)

# mytuple = ("minhaj", "jasim", "dilshad")
# if "dilshad" in mytuple:
#     print("yes you got it")
# k = list(mytuple)
# k.remove("nasiq")
# k.append("sinan")
# print(tuple(k))
# y = ("shamsu",)
# mytuple += y
# print(mytuple)

# (green, red, black) = mytuple
# print(green)
# print(red)
# print(black)


# for x in range(len(mytuple)):
#     print(mytuple[x])
# i = 0
# while i< len(mytuple):
#     print(mytuple[i])
#     i +=1
# mytuple1 = mytuple * 2
# print(mytuple1)

# fruits = {"apple", "orange", "mango","apple", "grape"}
# fruits1 = {"minhaj", "danish", "shahabas", "fahis"}
# fruits.update(fruits1)
# print(fruits)

# fruits.pop()
# print(fruits)
# set1 = {"a", "b", "c", "d"}
# set2 = {1,2,3,4}
# set4 = {12,432,5,212,4,2,12}
# set5 = {"minhj", "dilshaa", "jasi","shams"}

# set3 = set1 | set2 | set4 | set5
# print(set3)

# fruits = {"mango", "apple", "orange"}
# fruits1 = {"mango", "pineapple", "cherryy"}

# z = fruits & fruits1
# print(z)

# thisdict = {
#     "name" : "minhaj",
#     "age"  : 19,
#     "elctric": False,
#     "colors": ["red", "green", "white", "blue"],
#     "place" : "manjeri"
# }

# if "age" in thisdict:
#     print("yes got it")
# thisdict.popitem()
# del thisdict["colors"]
# thisdict.clear()
# for x in thisdict:
#     print(thisdict[x])

# for x , y in thisdict.items():
#     print(y,x)


# x = dict(thisdict)
# print(x)

# minhaj = {
#     "num1" : {
#         "name" : "minhaj",
#         "age" : 19,
#         "place" : "manjeri"
#     },
#     "num2" : {
#         "name" : "dilshad",
#         "age" : 23,
#         "place" : "areakode"
#     },
#     "num3" : {
#         "name" : "shamsu",
#         "age" : 22,
#         "place" : "mankada"
#     },
#     "num4" : {
#         "name" : "jasim",
#         "age" : 19,
#         "place" : "anakkayyam"
#     },

# }

# # print(minhaj["num2"] ["age"])

# for x, k in minhaj.items():
#     print(x)

#     for y in k:
#         print(y + ":" , k[y])
# a = "hello world"
# print(len(a))

# for x in "hello worls":
#     print(len(x))

# txt  = "my name is minhaj, iam from manjeri"
# print(txt.split("a"))

# a = "hello"
# b = "world"

# c = a + " " + b
# print(c)

# age = 35
# txt = f"my name is minhaj, my age is {20* 55} minhsd"
# print(txt)

# def myfunction(*kids):
#     print("the youngest child is  " + kids[2])

# myfunction("jacob", "minhaj", "yaseen", "dilshad")



# def check_scope():
#     def do_local():
#         test = "do local test"
#     def do_non_local():
#         nonlocal test
#         test = "do not local test"
#     def do_global_local():
#         global test
#         test = "global test"
    
#     test = "default"
#     do_local()
#     print("test value after do local " + test)
#     do_non_local()
#     print("test value after do non local " + test)

#     do_global_local()
#     print("test value after do global local " + test)
# check_scope()

# arbitary argument
# def finvtiona(*value):
#     print("second item is " + value[2])

# finvtiona("shs","dil", "min", "jas", "nas", "waf", "din")

# def func(name, place, age):
#     k = "name: " + name + " place: " + place + " age:" + age
    

# func(name = "minhaj", place="manjeri", age="18")

# i = 1
# while i <= 5:
#     j = 1
#     while j - 5:
#         print("*", end=(' '))
#         j += 1
#     print(" ")
#     i += 1

# class jam:
#     def do_local_host():
#         test = "local host"
#     def do_non_local():
#         nonlocal test
#         test="non local host"
#     def do_global_host():
#         global test
#         test = "global host"
        
#     test = "default"
#     do_local_host()
#     print("this is " + test)
#     do_non_local()
#     print("this is: " + test)
#     do_global_host()
#     print("this is  " + test)

# jam()
# print("this do global host is  " + test)

# if 1 == 2 :
#     print("1 is same in 1")
# else:
#     print("1 not same in 1")

# def totalSum(num1, num2):
#     total = num1 + num2 
#     return total+


# print(totalSum(10 , 21))

# x = "k"

# if x == "v":
#     print("violet")
# elif x == "i":
#     print("indigo")
# elif  x == "b":
#     print("blue")
# elif x == "g":
#     print("green")
# elif x == "y":
#     print("yellow")
# elif x == "o":
#     print("orange")
# elif x == "r":
#     print("red")
# else:
#     print("invalid color")  

# num = 10

# if num == 1:
#     print("sunday")
# elif num == 2:
#     print("monday")
# elif num == 3:
#     print("tuesday")
# elif num == 4:
#     print("wednesday")
# elif num == 5:
#     print("thursday")
# elif num == 6:
#     print("friday")
# elif num == 7:
#     print("saturday")
# else:
#     print("invalid number")

# x = 0
# while x < 10:
#     x +=1
#     if x == 5:
#         continue
#     print(x)    

# x = 2
# num = 5
# while x < num:
#     while j 

# x  = 1
# while x <= 10:
#     print(x,"hello")
#     x +=1
# else:
#     print("now the end is 1 to 10,thats all")

# num = 389
# i = 2
# limit = int(num/2)

# while i <= limit:
#     # print(num)
#     if num%i == 0:
#         print(f"{num} not a prime number")
#         break
#     i +=1
# else:
#         print(f"{num} is a prime number")
# i = 1
# limit = 5
# while i <= limit:
#     # print("*", end=" ")
#         k = 1
#         while k <= limit - i:
#             print(" ", end="")
#             k += 1
#         j = 1
#         while j <= i:
#               print("a", end=" ")
#               j += 1
#         print()
#         i += 1 



# emp_Age = [23,53,12,33,43,29]
# # emp_name = ["shamsu", "dilshad", "minhaj", "jasim"]
# # emp_Age.extend(emp_name)
# emp_Age.pop(4)
# print(emp_Age)

# age_limit = 5
# age_List = []
# i = 1
# while i <= age_limit:
#     age = int(input("enter a age : "))
#     age_List.append(age)
#     i += 1

# print(age_List)
# age_Sum = 0
# j=0
# while j < len(age_List):
#     age_Sum += age_List[j]
#     j+=1

# avarage = age_Sum/len(age_List)
# print(avarage)

# num_list = [21,32,55,66,54,12,43,22,100]

# max_value = 0
# j = 0
# while j < len(num_list):
#     if max_value < num_list[j]:
#         max_value = num_list[j]
#     j+=1

# print(max_value)



# num = 10
# end = int(num/2)+1
# for x in range(2, end):
#     if num%x== 0:
#         print("its a not prime number")
#         break
# else:
#     print("its a prime number")
# count = 0
# for x in range(100, 10, -1):
#     # if x%2 == 1:
#         print(x)

# number = []
# count = 0
# while True:
#     num = int(input("enter a number for 5 to 25"))
#     if num <= 25 and num >= 5:
#         number.append(num)
#         count +=1
#     else:
#         print(f"{num} is a invalid number")
#     if count == 5:
#         break
# print(number)



# name = "samosa"
# while name < len(name):


# limit = 6
# for x in range(limit):
#     for k in range(limit-x):
#         print(" ", end="")
#     for y in range(x):
#         print("*", end=" ")

#     print()

# i = 1
# m = 6
# while i <=  m:
#     for k in range(5):
#         print(i,k)
#     i +=1

# abc = [12,42,13,55,54,21,32]
# print(abc[::-1])

# a,b,c,d = (100,200,300,400)
# print(c)

# emp_salary = {
#     "minhaj" : 10000,
#     "shamsudheen" : 20000,
#     "dilshad" : 30000,
#     "jasim" : 23992,
#     "nasiq" : 32331,
#     "shammas" : 54382,
#     "maher ali" : 82322
# }
# for k in emp_salary.keys():
#     print(k)
# x = "shamsudheen"
# if x in emp_salary:
#     print(f"{x} is a inside the dictionary")
# else:
#     print(f"{x} this item not inside in the item")
# emp_salary.pop("jasim")
# emp_salary.
# print(emp_salary)
# for x in emp_salary.items():
#     print(x)

# x = dict(emp_salary)
# print(x)

# emp_salary = {}
# name = ["minhaj", "shamsudheen", "dilshad", "jasim"]
# salary = [1000,2000,3000,4000]

# for i in range(len(name)):
#     key = name[i]
#     value = salary[i]
#     emp_salary[key] = value

# print(emp_salary)


# car_model = {
#     "car1" : {
#         "name" : "wolkswogan",
#         "model":2000
#     },
#     "car2":{
#         "name": "maruti",
#         "model": 1998
#     },
#     "car3" : {
#         "name" : "benz",
#         "model" : 2022
#     },
#     "car4" : {
#         "name" : "audi",
#         "model": 2018
#     }
# }

# for x in car_model.pop("car2"):
    # print(x)
# car_model.update("name")
# print(car_model)

# car_model["car2"]["model"] = "2199"
# print(car_model)


# for x, obj in car_model.items():
#     print(x)

#     for y in obj:
#         print(y + ":", obj[y])


# new_List = ()
# new_List = (x*x*x for x in range(5) )
# print(new_List)

# new_dict = {x:x**2 for x in range(1,6)}
# print(new_dict)

# person = {"name": "Alice", "age": 30, "city": "New York"}
# person.pop("age")
# print(person)

# new_Dict = {x:x*x for x in range(1,11)}
# print(new_Dict)
# emp_Details = {}
# key_1 = ["name","age","city"]
# address = ["minhaj", 18, "manjeri"]

# for x in range(len(key_1)):
#     key = key_1[x]
#     value = address[x]
#     emp_Details[key] = value

# print(emp_Details)


# dict = {"a" : [1,2], "b" : [3,4] }
# dict.setdefault("c", [5])
# print(dict)

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list1.extend(list2)
# list1.insert(5)
# print(list1)


# numbers = (6,1,4,2,8,9,10) 
# print(numbers[4:])

# my_Tuple = (10,20,30,40,50)    
# my_Tuple2 = (11,12,13,14,15)
# my_Tuple3 = my_Tuple+my_Tuple2
# print(my_Tuple3)

# list1 =(1,2,3,4)
# list2 = [5,6,7,8]

# list2.extend(list1) 
# print(list2)


# my_Tuple = (100,200,300)
# a,b,c = my_Tuple
# print(a)
# print(b)
# print(c)

# my_list = [10, 20, 30, 40]
# print(my_list)
# k = tuple(my_list)
# print(k)
# x = list(k)
# print(x)

# def greet(x,y):
#     return x*y
# print(greet(2,5))

# def personel_info(name,age,city):
#     print("name is " + name)
#     print(age)
#     print("city is " + city)

# personel_info("minhaj",18,"manjeri")

# def sum_all(*args):
#     return sum(args)

# print(sum_all(10,20,40))

# def print_Details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# print_Details(name="minhaj", age=18, place="manjeri")

# counter = 0

# def increment():
#     # global counter
#     counter+=1

# increment()

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n* factorial(n-1)

# print(factorial(5))
        

# def min_max(numbers):
#     if len(numbers) == 0:
#         return None,None
#     return min(numbers),max(numbers)
    
    
# numbers = [10,2,10,3,23,93,22]
# min_value , max_value = min_max(numbers)
# # print(f"min: {min_value}, max: {max_value}")

# add_lambda = lambda x,y:x*y

# print(add_lambda(10,2))

# list1 = [1,2,3,4,5]
# squered_number = list(filter(lambda x: x%2==1, list1))
# print(squered_number)

# k = lambda x: x**2
# print(k(5))

# list1 = [1, 2, 3, 4, 5]
# squere_list= list(map(lambda x:x**2, list1))
# print(squere_list)
# even_num = list(filter(lambda x:x%2==0,list1))
# print(even_num)
# tottal = reduce(lambda x,y: x+y , list1)
# print(tottal)


# char =  ["apple", "is", "good", "at", "coding"]
# k = list(filter(lambda x: len(x) > 3, char))
# print(k)



# def decorate(func):
#     def changed():
#         result = func()
#         return result.upper()
#     return changed


# @decorate
# def name():
#     return "hello"

# print(name())


# def timer_decorator(func):
#     def inner_func():
#         result = func()
#         result = "hello world"
#         result.upper()
#         return result
#     return inner_func
# @timer_decorator
# def name():
#     return "goodmorning"

# print(name())


# def value(n):
#     if n == 1:
#         return 1
#     else:
#         return n* value(n - 1)

# print(value(5))


# k = lambda x,y:x+y

# print(k(20,32))

# list1 = [12,43,23,11,45]
# k = list(filter(lambda x: x < 30 , list1))

# print(k)

# result1 = difference.add(10,32)
# result2 = difference.substract(25,13)
# print(result1)
# print(result2)
# print(__name__)


# def outer(massage):
#     def inner():
#         print(massage)
#     return inner

# newar = outer("hello world")

# newar()

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# add_4 = outer(4)

# print(add_4(98))


# def outer(fun):
#     def inner():
#         result = fun()
#         # result.upper()
#         return result.upper()
#     return inner
# @outer
# def decor():
#     return "hello"

# print(decor())



# def recuir(n):
#     if n == 1:
#         return 1
#     else:
#         return n * recuir(n - 1)

# print(recuir(5))


# try:
#     a = int(input())
#     b = int(input())
#     c = a/b
# except ZeroDivisionError:
#     print("0 kond harikkunnathil valla arthavumundo?")
# except ValueError:
#     print("alphabet use cheyth aradaa ninne harikkan padippichee")
# else:
#     print(c)



# class person:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self,other):
#         return person(self.x + other.x, self.y + other.y) 
    
# p1 = person(12 +5)
# p2 = person(5 + 12)

# print(p1 + p2)

# class example:
#     def __add__(self,other):
#         return self + other
    
# num = 10
# num1 = 20

# result = example.__add__(num,num1)

# print(result)


# class example:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def start(self):
#         print(f"{self.age} is my age")
# address = example("minhaj", 18)
# address.start()



# class cars:
#     def __init__(self,name,model,color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def detail(self):
#         print(f"this is a {self.name} car,model is {self.model}, color is {self.color}")

# my_car = cars9("toyota", 1999 , "black")
# my_car.detail()


# class exm:
#     def __add__(self,x):
#         return self + x

# num = 10
# num1 = 20
# num3 = 30


# result = exm.__add__(exm.__add__(num,num1),num3)
# print(result)

# class exm:
#     def inner(self):
#         f = "hello"
#         print(f)

# class dupl(exm):
#     def inner(self):
#         f = "world"
#         print(f)
    
# class new1(dupl):
#     def inner(self):
#         f = "good morning"
#         print(f)

# k = new1()
# k.inner()




# def hello(*sum):
#     for x in sum:
#         print (f"hello, {x}!")
    

# hello("minhaj","shamsu", "dilshad") 

# def exmp(n):
#     if n == 1:
#         return 1
#     else:
#         return n * exmp(n - 1)
    
# print(exmp(5))


# list1 = [2,3,4,5]
# k = list(filter(lambda x: x == 4 ,list1))
# print(k)


# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print("please enter a number,value is not valid ")
# except ZeroDivisionError:
#     print("zerodivision error,please enter  above number")
# else:
#     print(c)
# finally:
#     print("finally successfully")


# def outer():
#     x = "local variable"
# def inner():
#     global x
#     x = "global variable"
#     return x
# print(x)

# def exch(func):
#     def wrapper():
#         print("suomthing before the function runs")
#         func()
#         print("something after thr function runs")
#     return wrapper        

# @exch
# def hello ():
#     print("hello")
# hello()


# list1 = [2,4,5,6]
# iterator = iter(list1)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# def my_generating():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# gener = my_generating()

# print(next(gener))
# print(next(gener))
# print(next(gener))
# print(next(gener))


# class hello:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

#     def pri(self):
#         print(f"my name is {self.name},am  {self.age} years old")

# person1 = hello("mminhaj", 18)

# print(person1.name)

# class good:
#     def hello(self):
#         print("goodd morning")
        


# class after(good):
#     def hello(self):
#         print("good aternoon")
    
# good = good()
# after = after()

# good.hello()
# after.hello()

# list1 = {x:x*x for x in range(1,20)}
# print(list1)

# fruits = ["banana", "orange", "mango","apple","cherry"]
# fruits.insert(1,"apple")
# print(fruits)

# for i in range(len(fruits)):
#     print(fruits[i])

# i = 0 
# while i < len(fruits):
#     print(fruits[i])
#     i += 1
# new_list1 = []
# for x in fruits:
#     if "a" in x:
#         new_list1.append(x)


# print(new_list1)

# class hello:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class moring(hello):
#     def good(self):
#         print(f"my name {self.name}, my age {self.age}")

# person1 = hello("minhaj", 18)

# moring.good(person1)

# class pont:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
    
#     def __add__(self,other):
#         if isinstance(other,pont):
#             return pont(self.x + other.x, self.y + self.x)
#         return NotImplemented

#     def __str__(self):
#         return f"pont({self.x}, {self.y})"

# p1 =  pont(10,20)
# p2 = pont(21,42)

# result = p1 + p2
# print(result)

# class point:
#     def __init__(self, x,y ):
#         self.x = x
#         self.y = y

#     def __add__(self,other):
#         if isinstance(other,point):
#             return point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"point({self.x}, {self.y})"
    
# p1 = point(10,21)
# p2= point(33,12)

# result = p1 + p2

# print(result)
# class single:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound"

# class multi:
#     def hello(self):
#         return f"{self.name} barks "


# class hier(single):
#     def hello(self):
#         return f"{self.name} kiiikkkkii"




# ulti = hier("dog")
# print(ulti.hello())



# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary

#     def hello(self):
#         return self.__salary

#     def set_salary(self,new_salary):
#         if new_salary > 0:
#             self.__salary=new_salary
#         else:
#             print("invalid salary")

# emp = employee("minhaj", 19)

# print(emp.name)
# print(emp.hello())

# emp.set_salary(4000)
# print(emp.hello())



# list1 = [10,20,30]

# k = iter(list1)

# print(next(k))
# print(next(k))
# print(next(k))


# def hello():
#     yield 10
#     yield 23
#     yield 32


# k = hello()
# print(next(k))
# print(next(k))
# print(next(k))

# keys = ['name', 'age', 'city']
# values = ['John', 25, 'New York']

# new_dict = dict(zip(keys,values))
# print(new_dict)

# def find_sum(**kwargs):
#     return sum (kwargs)
# sample_dict = {'a': 100, 'b': 200, 'c': 50}
# print(find_sum(sample_dict))


# x = "bananana"
# for i in x:
#     print(i)

# x = "hello, world, how are you guyss"
# word = "world"
# if word not in x:
#     print(f"{word} is not found")
# else:
#     print(f"{word}, this is find it")


# x = "hello, world"
# print(x.split(","))
# dict1 = {"name": "minhaj", "age": 18}
# dict2 = {"place" : "manjeri", "sex" : "male"}

# dict3 = {**dict1,**dict2}
# print(dict3)

# def count_vovel(check_value):
#     count = 0
#     vovels = "aeiou"
#     for x in check_value:
#         if x in vovels:
#             count+=1

#     return count

# k = count_vovel("hello world")
# print(k)    

# word = "hello world"
# count = 0
# vovels = "aeiou"
# for x in word:
#     if x in vovels:
#         count += 1
# print(count)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# class car:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model

#     def display_info(self):
#         return f"{self.make} : {self.model}"

# k = car("bmw",2022)
# print(k.display_info())


# a = "Hello"
# b = "world"
# a,b = b,a
# print(a)
# print(b)

list1 = [11,22,"minhaj", False,True]
print(list1)