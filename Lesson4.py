
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
def payroll(basic_salary,transport, water):
    # basic_salary = 50000
    # transport = 3000
    # water = 1500
    nhif = 500
    gross_pay = basic_salary + transport + water
    print('Your Gross Salary is ', gross_pay)

# this function is more reusable
payroll(basic_salary=30000,transport=4500,water=1500)
payroll(basic_salary=28000, transport=3500,water=2500)
payroll(water=2300, transport=4500,basic_salary=75000)
try:
   payroll(basic_salary=80000)
except TypeError as type_error:
    print('Error Occured ', type_error)
except:
    print('Something else is wrong')







