import sys
sys.path.append('/home/mahesh/Documents/import_modules')
import datetime
import calendar
import os
#from import_modules import find_index, test  # when we import other modules. if any print statement it contains it print those also.
"""It's check multiple location by using sys.path """

#from import_modules import * # import everything.


courses = ['History', 'Math', 'physics', 'Compsci']

#index = find_index(courses,'Math')
# print(index)

# print(test)
print(sys.path)
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)
