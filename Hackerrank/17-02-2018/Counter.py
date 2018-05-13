import collections

no_shoes = int(input())
shoes_list = collections.Counter(map(int, input().split()))
no_cust = int(input())
income = 0
for i in range(no_cust):
    size, price = map(int, input().split())
    if shoes_list[size]: 
        income += price
        shoes_list[size] -= 1

print(income)
