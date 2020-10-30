
# Exceptions and Functions
try:
    person = {'john':40, 'peter':45}
    print(person['hassan'])
    f = open("modcom.txt", "r")

except KeyError as key_error:
    print('Error Occured1!', key_error)

except FileNotFoundError as file_error:
    print('Error Occured2!', file_error)

except:
    print('Something is wrong')

finally:
    print('Close connections')
    # it will execute regardless if an error is raised or not
