import pandas as pd

address = '2/119 Railway St N'

exclude_list = ['N', 'S', 'W', 'E']
address_list = address.split(' ')
print(address_list)
street_type = address_list[-1]

if street_type in exclude_list:
    street_type = address_list[-2]

print(street_type)





# 2/119 Railway St N
# 9/400 Dandenong Rd
# 172 Danks St