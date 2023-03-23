#Topic: Dictionaries in Python
#dictionaries are unordered collection of keys and values

#defining a dict
my_dict = {'name':'Adil', 'Age':22}

#accessing value from dict
print(my_dict['name'])

#printing keys in dict
print(my_dict.keys())

#printing the values of the dict
print(my_dict.values())

#adding values in dict
my_dict['university'] = 'FAST-NUCES'
print(my_dict['university'])
print(my_dict.keys())

#removing values from dict
my_dict.pop('university')
print(my_dict.keys())

#modifying values in dict
my_dict['Age'] = 25
print(my_dict['Age'])

