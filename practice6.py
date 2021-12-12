# 다음 출력과 같은 모양으로 출력하세요.
for a in range(1, 6):
    for b in range(5 - a):
        print(" ", end="")
    for c in range(a):
        print('*', end="")

    print()