import numpy as np


def random_predict(number: int = 1) -> int:
    a=50
    count = 0
    predict_number = a
    while True:
        a = int(a//2)
        if a == 0:
            a = 1
        count += 1
        if number == predict_number:
            break  
        elif number > predict_number:
            predict_number += a
        elif number < predict_number:
            predict_number -= a
    return count


def score_game(random_predict) -> int:
    count_ls = []
    #np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)