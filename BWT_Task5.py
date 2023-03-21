#Enumerate Function
#this function loops over any iterable object then assigns them an index
fav_food = ['pizza', 'karahi', 'burger', 'chocolate icecream']
for i, fav_food in enumerate(fav_food):
	print(i, fav_food)

#user inputs
#exercise 7.1
car = input('What kind of rental car would you like?\nAnswer:')
print('Let me see if we can find you a', car)	 

#conditionals
x = 5
if x > 0:
	print('number is positive')
elif x < 0:
	print('number is negative')
else:
	print('number is 0')
		
#sets and set operations
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.difference(my_set2))
print(my_set2.difference(my_set1))
