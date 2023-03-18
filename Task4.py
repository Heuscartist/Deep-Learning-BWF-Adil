#exercise 3.1 -- Names
names = ['ali', 'abdullah', 'fahad', 'rohaan']
print(names[0], names[1], names[2], names[3])

#exercise 3.2 -- Greetings
greetings = ['Hello Ali, how are you?', 'Great to see you Abdullah!']
print(greetings[1])

#exercise 3.3 -- Your Own List
transportation = ['toyota', 'honda']
print('I would like to buy a ' + transportation[0])

#exercise 3.4 -- Guest List
people = ['Bob Ross', 'Muhammad Ali']
print('Mr.' + people[0] + ', I would like to invite you to dinner ')
print('Mr.' + people[1] + ', I would like to invite you to dinner ')

#exercise 3.5 -- Changing Guest
people[0] = 'Isaac Newton'
print('Mr.' + people[0] + ', I would like to invite you to dinner ')
print('There are', len(people) , 'people coming to the dinner')

#exercise 3.6 -- More Guests
people.insert(0, 'Bob Ross')
people.insert(len(people), 'Ali')
people.append('Naseeb')
print(people)

#exercise looping
for guests in people:
	print(guests)

#exercise 4.1 -- Pizza
pizzas = ['fajita', 'pepperoni', 'margherita']
for flavors in pizzas:
	print(flavors)	

#exercise sorting / reversing
pizzas.reverse()
print(pizzas)
print(sorted(pizzas))


#exercise 4.3 -- Count to 20
for value in range(21):
	print(value)

#exercise 4.6 -- Odd numbers till 20
for value in range(1,21,2):
	print(value)


cubes  = [values**3 for values in range(11)]
print(cubes)
