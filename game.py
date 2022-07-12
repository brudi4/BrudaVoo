import numpy as np

number = np.random.randint(1, 10)
counter = 0
while True:
    num = int(input('Vvedite chislo: '))
    counter += 1
    if number > num:
        print(f'Nashe chislo bolshe, chem {num}.')
    if number < num:
        print(f'Nashe chislo menshe, chem {num}.')
    if num == number:
        print('Nice!')
        break

print(f'Ti ugadal chislo za {counter} raz, GG!')