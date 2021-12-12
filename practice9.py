# 구구단의 “단”을 입력 받아 해당 “단”의 구구단을 출력하는 함수로 작성하세요.

def gugudan(dan):
    for i in range(1, 10):
        print(f'{dan} * {i} = {dan * i}')

number = int(input('단을 입력하세요: '))
gugudan(number)