a = int(input())
dp = [0,1,3]

for i in range(3, a + 1) :
  dp.append(dp[i - 1] + dp[i - 2] * 2)
print(dp[a] % 10007)
