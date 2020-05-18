
x = 1
if x == 1 :
    print("x is ",  x)

while x != 10:
    print(x)
    x += 1
    
print("Done!")

# https://www.learnpython.org/en/Variables_and_Types

one = 1
two = 2
three = one + two

print( "one + two = ", three )

hello = "hello"
world = "world"

print( hello + " " + world)

a,b = 3,4
print(a,b)

print("String replacement: %s is %d years old." % ("Eric", 23) )

# https://www.learnpython.org/en/Lists

numbers = []
strings = []
names = ["John","Eric","Jessica"]

second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("One")
strings.append("Two")
strings.append("Three")

print(numbers)
print(strings)
print("The second name on the names list is %s." % second_name)

# basic operators

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2** 3
print(squared)
print(cubed)

print("Hello" + " " + "World")

lots_of_hellos = "hello..." * 10
print(lots_of_hellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([9,8,7] * 3)

# test
# objective: 10 instances and concat both into big_list
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print( "x_list contains %d objects" % len(x_list))
print( "y_list contains %d objects" % len(y_list))
print( "big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
	print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
	print("Great!")


# strings

print("Strings are %s and %d of them are better. %f floats are wild, but %.2f contained floats are best. What about %s arrays/lists!? " % ("cool",25, 5.1241613, 5.1241613, [1,2,3])) 

print("String len(%s) = %d " % ("This is the total length of this string...",len("This is the total length of this string...")))

a_string = "This is a totally new string."
print("The index for 'o' in this string, '%s', is '%d'. " % (a_string, a_string.index("o")))
print("The count for 'o' in this string, '%s', is '%d'. " % (a_string, a_string.count("o")))
print("The array call [11:25] in this string, '%s', is '%s'. " % (a_string, a_string[11:25]))
print("The sliced string [11:25:2] in this string, '%s', is '%s'. " % (a_string, a_string[11:25:2]))
print("The sliced string reverse [::-1] in this string, '%s', is '%s'. " % (a_string, a_string[::-1]))
print("The string upper() and lower() in this string, '%s', is '%s' and '%s'. " % (a_string, a_string.upper(), a_string.lower()))
print("String starts with 'This' = %s (case sensitive). " % a_string.startswith("This"))
print("String ends with 'afadgsdg' = %s (case sensitive). " % a_string.endswith("afadgsdg"))
print("String split at space = '%s' " % a_string.split(" "))

# string[from:to:slice]


# conditions
x = 2
print( x == 2)
print( x == 3)
print( x < 3)

y = 19
if x > 1 and y < 20:
	print("AND Conditions are met 01")

if x < 5 or y > 20:
	print("OR Conditions are met 02")


if "John" in ["Eric","John","Sam"]:
	print("John was in array of names.")
	pass
elif "John" in ["new","list"]:
	print("else if (elif) condition met.")
	pass
else:
	pass

y = 2
print( x is y)
print( "False bool using not = %s " % (not False) )


# loops

for x in range(5):
	print(x)

print("break...")
for x in range(3,6):
	print(x)
print("break...")
for x in range(3,8,2):
	print(x)
print("break...")

count = 0
while count < 15:
	print("While count #%d" % count)
	count += 1

count = 0
while True:
	count+=1
	if count >= 15:
		break

	if count % 2 == 0:
		continue

	print("While using break/continue, #%d" % count)
else:
	print("While loop finished.")

for x in range(10):
	print("For loop x in range(10) = %d " % x)
else:
	print("For loop complete.")



# functions

def my_function(user, age):
	print("Welcome %s, you still look splendid, even at %d!" % (user,age))

my_function("Josh",24)

# classes & objects

class myClass:
	variable = "blah"

	def help(self):
		print("Function in class ")

obj = myClass()

print("Accesing class objects. obj.variable = %s" % obj.variable)
obj.variable = "new variable"
print("Changing then Accesing class objects. obj.variable = %s" % obj.variable)

obj.help()


# dictionaries
# dics are data types

phonebook = {}
phonebook["John"] = 5556421
phonebook["Sarah"] = 5579421
phonebook["Sam"] = 500721

print(phonebook)

# or

phonebook = {
	"John" : 3456789,
	"Sam" : 2345622,
	"Jill" : 13513535,
}

print(phonebook)

for name, number in phonebook.items():
	print("Phone number for %s is %d " % (name,number))

del phonebook["Sam"] # or 

if "Sam" in phonebook:
	phonebook.pop("Sam")
if "Sam" not in phonebook:
	phonebook["New Sam"] = 12432542

print("Removed Sam and added New Sam")
print(phonebook)


# modules

import urllib
#urllib.parse("https://www.google.com/")
help(urllib)