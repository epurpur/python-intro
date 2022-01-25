



#Strings & variables
variable1 = "apple"
variable2 = "1234"
variable3 = "abc123"
variable4 = "this is also a string"






#Print Statement - A built-in function used to write output to console or elsewhere
print("hello world")
print(variable1)






##Numbers (Ints and Floats)
number1 = 4
number2 = 3.14
number3 = 4 + 1
number4 = number1 + 1
number5 = variable1 + variable2
#number6 = number1 + variable1






#Error Messages - Read them from the bottom up. Get used to reading error messages!
print('hello world)



#Lists, loops, booleans, and indexing

#it is very common to add and remove things from lists
cities = ['New York', 'London', 'Bangkok', 'Tokyo', 'Sydney']

print(cities)
cities.append('Charlottesville')
print(cities)
cities.remove('London')
print(cities)

numbers = [1, 2, 3, 4, 5]
for number in numbers:                         #for loop
    print(number)

for city in cities:
    print(city)
    
for i in cities:
    print(i)
    
print(cities[1])

z = 1
while z < 10:                                  #while loop
    print(z)
    z = z + 1

b = 7
while b < 10:                                  #watch out for endless loop!
    print("B is less than 10")


      
      
    
#Conditionals (if, elif, else)
x = random.randint(0, 20)
print("x = ", x)

if x > 12:
    print("x is greater than 12")
elif x < 8:
    print("x is less than 10")
else:
    print("x is somewhere in the middle")


#Functions. Functions are used to write re-usable code. And to use other people's code
#built-ins like print(), type(). These are a part of the python standard library

number1 = 4
print(number1)
print("Number 1 =", number1)
print(type(number1))
print(type(number2))

def function1():
    print("This is running from inside function1")
function1()

def adding_function(number):                               #passing in a variable as argument to the function
    print("Old number =", number)
    a = 2
    new_number = number + a
    print("New number =", new_number)
adding_function(5)
      
    
      
      
    
#Dictionaries  (key, value pairs)
athletes = {'Michael Jordan': 'Basketball',
            'Wayne Gretzky': 'Hockey',
            'Leo Messi': 'Soccer',
            'Roger Federer': 'Tennis'}

for keys, values in athletes.items():
    print(keys,"plays", values)

for values in athletes.values():
    print(values)
    
print(athletes['Michael Jordan'])
print(athletes[2])                             #dicts do not support indexing!

athletes['Peyton Manning'] = 'Football'
print(athletes)

MLB_Teams = {'Boston Red Sox': ['American League', 'Massachusetts', 'Fenway Park'],
            'New York Yankees': ['American League', 'New York', 'Yankee Stadium'],
            'Chicago Cubs': ['National League', 'Chicago', 'Wrigley Field']}








#Import (from other libraries, files, etc)
#This lets you bring in code from other places and is hugely powerful
import random
print(random.randint(0,20))
    
    



#Mutable and Immutable data types
Some data types can be changed, others cant

tuple1 = (0, 1, 2, 3)              #use tuples for performance. When things probably aren't going to be changed.
tuple1[0] = 5
print(tuple1)

list1 = ['blue', 'red', 'yellow', 'orange']
print(list1)
list1[0] = 'green'
print(list1)


