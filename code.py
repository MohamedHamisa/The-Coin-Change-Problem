def getWays(n, c):
    dp = [1] + [0] * n
    for c in c:
        for i in range(c, n+1):
            dp[i] = dp[i] + dp[i-c]
    return dp[-1]
  
  



