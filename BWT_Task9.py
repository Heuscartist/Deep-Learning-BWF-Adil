

#Example 10.1
filename = 'task9_reading.txt'

with open(filename) as file_object:
	contents = file_object.read()
	print(contents)
file_object.close()

#Example 10.3
name = input('Input your name: ')
with open('write_file.txt', 'w') as file_object:
	file_object.write(name)


#Exceptions
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
	
	
#Example 10.6
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = a + b
        print(a, "+", b, "=", c)
        break
    except ValueError:
        print("Enter a valid number.")
 
 
        
cat_file = 'cats.txt'
dog_file = 'dogs.txt'

try:
    with open(cat_file) as file_object:
        cats = file_object.readlines()
    with open(dog_file) as file_object:
        dogs = file_object.readlines()
except FileNotFoundError:
    print("Sorry, one of the files is missing.")
else:
    print("Cats:")
    for cat in cats:
        print(cat.rstrip())
    print("\nDogs:")
    for dog in dogs:
        print(dog.rstrip())


