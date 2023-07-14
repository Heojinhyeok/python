import time

n = 0
while True:
    if n >= 5:
        print('[ WARN ] 5초동안 기다리세요 ㅗ')
        time.sleep(5)
    nums = input('비밀번호 입력: ')

    if nums == '3415':
        print('[ OK ] 현관문이 열렸습니다.')
        break
    else:
        print('[ FAIL ] 비밀번호가 틀렸습니다.')
        n += 1
        continue
