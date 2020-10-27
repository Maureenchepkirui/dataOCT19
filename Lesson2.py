# lists,tuples, dictionary, loops
# What is a list  - is a collection of items stored in one variable
counties = ['Embu','Kisumu','Nakuru','Nairobi','Mombasa']
print(counties)

budgets = [500000, 200000,600000, 800000,700000,1000000]
print(budgets)

# slicing lists
print('I come from ', counties[4], 'County')
print('I will visit ', counties[1:4])  # -1
print('My budget is ', budgets[3])

# What is a tuple  - is a collection of items stored in one variable
cars = ('Toyota','Nissan','BMW','Honda','Volvo')
print(cars)

cost = (700000,850000,1000000,450000)
print(cost)
# slicing tuple
print(' A ', cars[1], 'will be valued at ', cost[1], 'KES')
print('I will buy a ', cars[3], '@', cost[0], 'KES')

# 1st difference - list uses [], tuple uses ()
# 2nd difference - lists can be updated - mutable, tuple cannot be updated - immutable
counties.append('Kajiado')
counties.remove('Nakuru')
print(counties)

# You want to send data somewhere, and it can't be added or removed in transit-tuple

# What is a dictionary  - its like an object.
phone = {'name':'Nokia',
         'cost':10000,
         'memory': '2GB',
         'OS': 'Android',
         'Version':5.0}

print(phone)
# use the key to retrieve
print(phone['name'])




