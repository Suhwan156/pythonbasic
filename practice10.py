"""1~10까지의 정수 리스트를 map함수와 lambda를 이용해 각 요소를
아래의 함수에 대입한 결과 값을 리스트를 생성하는 프로그램을
작성하세요. """

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fx = map(lambda x: (2 * x + 1), input_list)
print(list(fx))
