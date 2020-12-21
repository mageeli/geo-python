# Create and print a dictionary
mydict = {
    "first name": 'Mousa',
    "last name": 'Ageeli',
    "age": 33,
    "SEU NO": 'g200007195'
}
print(mydict)

# Accessing items in a dictionary
age = mydict['age']
print(age)

# Looping items through a dictionary
for key, val in mydict.items():
    print(key, "=>", val)

# Change a value in a dictionary
mydict['age'] = 120
print(mydict)

# Check if key exists in a dictionary
if "age" in mydict:
    print('yes')

# Print a dictionary length
print(len(mydict))

# Adding Items to a dictionary
mydict['car color'] = 'white'
print(mydict)

# Removing Items in a dictionary
del mydict['car color']
print(mydict)
