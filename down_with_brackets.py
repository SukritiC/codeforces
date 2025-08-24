def solve():
    s = input().strip()
    n = len(s)
    balance = 0


    for i in range(n - 1):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1


        if balance == 0:
            print("YES")
            return


    print("NO")



t = int(input())
for _ in range(t):
    solve()