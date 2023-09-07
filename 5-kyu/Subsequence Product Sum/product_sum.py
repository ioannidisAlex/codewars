def product_sum(a, m):
    dp = { (i,j):0 for i in range(len(a)) for j in range(m) }
    sum_of_mine = 0
    for i in range(len(a)):
        for ix in range(min(i+1,m)):
            if ix == 0:
                sum_of_mine += a[i]
                dp[i,0] = sum_of_mine 
            elif ix == i:
                dp[ix,ix] = dp[ix-1,ix-1]*a[ix]
                break
            else:
                dp[i,ix] = a[i] * (dp[i-1,ix-1]) + dp[i-1,ix]
    return dp[len(a)-1,m-1] % (10**9 + 7)
