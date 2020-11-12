def func(a) :
    dp = [1, 1, 3]
    for i in range(3, a + 1):
        dp.append(dp[i - 1] + dp[i - 2] * 2)
    return dp[a]

while True :
    try :
        a = int(input())
        print(func(a))
    except :
        break
