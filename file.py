num1 = 42 #variable declaration, initialize, number
num2 = 2.3 #variable declaration, initialize, number
boolean = True #variable, initialize, boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, string, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, Boolean, initialize set
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize set
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, acccess value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #log statement, function, access value
person['name'] = 'George' #set, change value - NOT ALLOWED IN SET
person['eye_color'] = 'blue' #set, add value
print(fruit[2]) #tuple, access value

if num1 > 45: #conditional, if
    print("It's greater") #log statement, string
else: #conditional, else
    print("It's lower") #log statment, string

if len(string) < 5: #conditional, if, length check
    print("It's a short word!") #log statement, string
elif len(string) > 15: #conditional, else if, length check
    print("It's a long word!") #log statement, string
else: #conditional, else
    print("Just right!") #log statement, string

for x in range(5): #for loop, range
    print(x) #log statement
for x in range(2,5): #for loop, range, start, stop
    print(x) #log statement
for x in range(2,10,3): #for loop, range
    print(x) #log statement
x = 0 #variable declaration, initialize
while(x < 5): #conditional, while
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() #list
pizza_toppings.pop(1) #list, delete value

print(person) #log statement
person.pop('eye_color') #list, delete value
print(person) #log statement

for topping in pizza_toppings: #for loop, list
    if topping == 'Pepperoni': #conditional, list
        continue #continue
    print('After 1st if statement') #log statement, string
    if topping == 'Olives': #conditional, if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #conditional, for loop, range
        print('Hello') #log statement, string

print_hello_ten_times() #function, no argument

def print_hello_x_times(x): #function
    for num in range(x): #conditional, for loop
        print('Hello') #log statement, string

print_hello_x_times(4) #argument

def print_hello_x_or_ten_times(x = 10): #function, 
    for num in range(x): #conditional, range
        print('Hello') #log statement, string

print_hello_x_or_ten_times() #function, no argument
print_hello_x_or_ten_times(4) #function, argument


"""
Bonus section
"""

# print(num3) NameError: num3 is not defined
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1) IndexError: list index out of range