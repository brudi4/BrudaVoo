import pandas as pd

test_experience = 'Опыт работы 8 лет 3 месяца'

current_experience = 0
test_experience = test_experience.split(' ')
print(test_experience)

years_list = ['лет','год','года']
months_list = ['месяца','месяцев','месяц']


if test_experience[3] in years_list:
    current_experience = int(test_experience[2])*12 + int(test_experience[4])
elif test_experience[3] in months_list:
    current_experience = int(test_experience[2])

