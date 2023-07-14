import random
import time

# 1. 로또 번호 목록 만들기
# lotto_nums_lists = [1, 2, 3, 4, 5, ...., 44, 45]
lotto_nums_lists = []
for i in range(1, 46):
    lotto_nums_lists.append(i)

# 2. 로또 번호 섞기 -> 번호 뽑기
sec = 0.5
secs = 0
i = 1
results = []
while True:
    random.shuffle(lotto_nums_lists)
    time.sleep(sec)
    secs += 2

    if secs % 6 == 0:
        if i > 6:
            break
        results.append(lotto_nums_lists.pop())
        #print(i, '번째:', ' '.join(results))
        i += 1
