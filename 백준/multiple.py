A = int(input())  # input을 숫자로 받음
B = input()       # input을 문자열로 받음

# 3자리 숫자일 때만 가능

AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep="\n")
# sep="\n" : 결과를 각각 다른 줄로 출력함