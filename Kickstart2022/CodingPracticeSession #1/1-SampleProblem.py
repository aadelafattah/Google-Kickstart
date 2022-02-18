def solve(case_num):
    bags, kids = map(int, input().split())
    candy = list(map(int, input().split()))
    sum = 0
    for i in range(bags):
        sum += candy[i]
    print(f"Case #{case_num}: {sum%kids}")

test = int(input())
for i in range(test):
    solve(i+1)