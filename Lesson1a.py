
# lets create a program to find body mass index
# You take your weight divide by height squared

height = float(input('What is your height'))
weight = float(input('What is your weight'))
person_name = str(input('What is your name'))

# Do Maths
body_mass_index = weight/(height * height)
print('Your BMI is ', body_mass_index, ' Your Name was ',person_name)




