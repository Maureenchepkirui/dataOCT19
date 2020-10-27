
# lets create a program to find body mass index
# You take your weight divide by height squared

height = float(input('What is your height'))
weight = float(input('What is your weight'))
person_name = str(input('What is your name'))

# Do Maths
body_mass_index = weight/(height * height)
print('Your BMI is ', body_mass_index, ' Your Name was ',person_name)

# concatenation: mixing a 'string' and a variable
# Decision making/Control Structures
# we use if, if else, elif
if body_mass_index < 17.5:
    print('Underweight')

elif body_mass_index >= 17.5 and body_mass_index < 22.5:
    print('Normal')

else:
    print('Overweight') # above 22.5


# Mon: 8.00 - 11.00, Mon: 2 - 4
# Wed: 8.00 = 11.00  Mon - 2 - 4
#






