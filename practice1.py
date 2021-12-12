# 학생 김동국의 국어/영어/수학 점수를 입력 받아 평균을 구하는 프로그램을 작성하세요.

korean, english, math = map(float, input('김동국의 국어 영어 수학 점수를 입력하세요 : ').split())
average = (korean + english + math) / 3
print('김동국의 평균 점수는 %.2f입니다.' % average)