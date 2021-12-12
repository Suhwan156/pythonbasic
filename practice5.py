# 연도를 입력 받아 해당 연도의 띠를 출력하는 프로그램을 작성하세요

birth_year = int(input("연도를 입력하세요 : "))
year = birth_year % 12

if year == 0:
    print("원숭이띠")

elif year == 1:
    print("닭띠")

elif year == 2:
    print("개띠")

elif year == 3:
    print("돼지띠")

elif year == 4:
    print("쥐띠")

elif year == 5:
    print("소띠")

elif year == 6:
    print("범띠")

elif year == 7:
    print("토끼띠")

elif year == 8:
    print("용띠")

elif year == 9:
    print("뱀띠")

elif year == 10:
    print("말띠")

else:
    print("양띠")
