#Task# 8 -- BWT - Deep Learning Track
#Classes and Inheritance
#Adil Mubashir Chaudhry

#Exercise 9.1 -- Restraunt

class restraunt():
	"""
	A simple restraunt class
	"""
	
	def __init__(self, name, cuisine_type, number_served = 0):
		"""Initializing the class attributes"""
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = number_served	#exercise 9.4 update

	def describe_restraunt(self):
		"""Prints the attributes of the restraint"""
		print('Restraunt Desciption: ' + self.name + " ", self.cuisine_type)
	
	def is_open(self):
		"""Prints that Restraunt is Open"""
		print(self.name + ' is open')
	
	def set_number_served(self, new_served):
		self.number_served = new_served
	
	def increment_number_served(self):
		self.number_served += 1
		
	def print_number_served(self):
		print('People Served at ', self.name, ':', self.number_served)
	
	
class IceCreamStand(restraunt):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'vanilla']

    def print_flavors(self):
        print('We have the following flavors available: ', self.flavors)	

#Exercise 9.2 -- Creating Multiple Instances of the Restraunt Class
a = restraunt('Restraunt A', 'Desi')
a.describe_restraunt()
a.is_open()
a.print_number_served()
	
b = restraunt('Restraunt B', 'Italian')
b.describe_restraunt()
b.is_open()
b.set_number_served(5)
b.print_number_served()	
	
c = restraunt('Restraunt C', 'Fast Food')
c.describe_restraunt()
c.is_open()
c.set_number_served(10)
c.increment_number_served()
c.print_number_served()


ice_cream_store = IceCreamStand('Adils IceCream')
ice_cream_store.describe_restraunt()
ice_cream_store.print_flavors()
	
