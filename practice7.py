# random으로 생성한 정수(1~100)와 사용자가 입력한 정수가 동일할 때까지 반복하는 프로그램을 작성하세요.
# ▪ 정답이 입력 받은 정수보다 큰 경우 “정답이 크다”라는 힌트 출력
# ▪ 정답이 입력 받은 정수보다 작은 경우 “정답이 작다”라는 힌트 출력
# ▪ 정답인 경우 “정답입니다”를 출력 후 종료

import random
random_number = random.randrange(1, 101)

while True:
    answer_number = int(input('정답을 입력하세요: '))

    if random_number > answer_number:
        print(f'정답은 {answer_number}보다 큽니다.')
    elif random_number < answer_number:
        print(f'정답은 {answer_number}보다 작습니다.')
    else:
        print('정답입니다.')
        break
