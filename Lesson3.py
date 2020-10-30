
# Exceptions and Functions
try:
    person = {'john':40, 'peter':45}
    print(person['hassan'])
except:
    print('Error Occured!')
    # Exception try, except
finally:
    print('Close connections')
    # it will execute regardless if an error is raised or not
