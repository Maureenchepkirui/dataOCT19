
# functional way
# functional is a block of codes/statements that perform specif task
# Advantages: split your into small bits, easy to use, maintain, understand code
#             Code re use - use existing code to build new code
#             Used in Object Oriented Programming
# 1
def body_mass_index():
    weight = 89.8
    height = 1.4
    bmi = weight/(height*height)
    print('Your BMI ', bmi)

# Function must be invoked/used/call/trigger
body_mass_index()

# 2
def simple_interest():
    principle = 60000
    rate = 12.5
    time = 36

    interest = (principle*rate*time)/100
    print('Your SI is ', interest)

simple_interest()
simple_interest()
simple_interest()


# making a function more dynamic, we use paramters
# payroll function
def payroll():
    basic_salary = 50000
    transport = 3000
    water = 1500
    nhif = 500

    gross_pay = basic_salary + transport + water
    print('Your Gross Salary is ', gross_pay)


payroll()
payroll()








