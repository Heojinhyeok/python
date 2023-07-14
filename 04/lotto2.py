import random
import time


def create_lotto_nums_lists():
    return [i for i in range(1, 46)]


def lotto_shuffle_and_pick(numlist, s, max):
    print('Pleas wait a miniute... please...')
    lotto_nums_lists = numlist
    sec = s
    secs = 0
    i = 1
    results = []
    while True:
        random.shuffle(lotto_nums_lists)
        time.sleep(sec)
        secs += 2

        if secs % 6 == 0:
            if i > max:
                break
            results.append(lotto_nums_lists.pop())
            # print(i, '번째:', ' '.join(results))
            i += 1

    return results


def print_lotto(lo):
    for i in lo:
        print(i, end=' ')


def lotto_number(max_choice):
    lotto_nums_lists = create_lotto_nums_lists()
    lotto = lotto_shuffle_and_pick(lotto_nums_lists, 0.5, max_choice)
    # print(lotto)
    print_lotto(lotto)


def main():
    lotto_number(6)

if __name__ == '__main__':
    main()
    