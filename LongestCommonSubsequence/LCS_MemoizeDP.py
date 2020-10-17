def lcs(a,b,n,m,ans,dp):

    if n==0 or m==0:
        return 0

    if dp[m][n]!=-1:
        return dp[m][n]

    if a[n-1]==b[m-1]:
        dp[m][n]=1+lcs(a,b,n-1,m-1,ans,dp)
    else:
        ans1=lcs(a,b,n-1,m,ans,dp)
        ans2=lcs(a,b,n,m-1,ans,dp)
        dp[m][n]=max(ans1,ans2)

    return dp[m][n]



# main
a=str(input())
n=len(a)
b=str(input())
m=len(b)
dp=[[-1 for i in range(m+1)]for i in range(n+1)]
print(lcs(a,b,n,m,0,dp))