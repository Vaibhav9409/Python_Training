# import sys
# for path in sys.path:
#     print(path)

import module_1
print(module_1.patient)
#module_1.print_details()


import module_1 as m1
print(m1.patient)
#m1.print_details()


from module_1 import patient
print(patient)

from module_1 import *
print(patient)
print_details(patient)
