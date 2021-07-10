# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
coin_list = []
# int로 변환할 때 map 함수 사용

for _ in range(N):
    coin = int(input())
    coin_list.append(coin)

count = 0

while K != 0:
    coin_pop = coin_list.pop()
    count += (K//coin_pop)
    K = K%coin_pop

print(count)