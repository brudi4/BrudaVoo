import numpy as np

def random_predict(number):
    counter = 0
    while True:
        num = np.random.randint(1,10)
        counter += 1
        if num == number:
            break
    return counter

def score_game(random_predict):
    counters_list = []
    nums_to_guess = np.random.randint(1,10, size=(50))
    for i in nums_to_guess:
        counters_list.append(random_predict(i))
    srednee = np.mean(counters_list)
    return srednee

print(f'Srednee kolichestvo popitok ugadivaniya: {score_game(random_predict)}')

print('Cool!')

<<<<<<< HEAD

=======
>>>>>>> 269f33a (asdsad)
if __name__ == '__main__':
    score_game(random_predict)