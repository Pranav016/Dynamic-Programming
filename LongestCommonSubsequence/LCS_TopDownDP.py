def lcs(a,b,n,m,dp):

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])

    return dp[n][m]


# main
a=str(input())
n=len(a)
b=str(input())
m=len(b)
dp=[[-1 for i in range(m+1)]for i in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            dp[i][j]=0
print(lcs(a,b,n,m,dp))