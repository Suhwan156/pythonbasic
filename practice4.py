# 정수를 입력 받아 2의 배수인지 3의 배수인지 확인하는 프로그램을 작성하세요.

while True:
    a = int(input('정수를 입력하세요: '))


    if a == 0:
        print('0을 입력하셨습니다')
    elif (a % 2 == 0) and (a % 3 == 0):
        print('2와 3 모두의 배수입니다')
    elif a % 2 == 0:
        print('2의 배수입니다')
    elif a % 3 == 0:
        print('3의 배수입니다')
    else:
        print('2와 3 모두의 배수가 아닙니다.')