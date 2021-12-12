# 문자열을 입력 받아 압축하는 프로그램을 작성하세요
s = str(input('압축할 문자열을 입력하세요: '))

result = s[0]  # 첫번째 값을 결과에 넣는다
count = 0   #

for st in s:
    if st == result[-1]:  #
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print(result)

