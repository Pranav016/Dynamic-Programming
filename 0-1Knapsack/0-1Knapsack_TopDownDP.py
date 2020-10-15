# In Top Down approach we first always make a table, recursion calls are emitted in Top down apprach. It is an iterative approach.
# Top Down approach can be better than memoized and recursive since it cannot have an issue of Stack Overflow.


def knapsack(wt,val,cap,n,dp):
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if wt[i-1]<=j:
                includeThisWt=val[i-1]+dp[i-1][j-wt[i-1]]
                notIncludeThisWt=dp[i-1][j]
                dp[i][j]=max(includeThisWt,notIncludeThisWt)
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][cap]


# main
n=int(input()) # size of the array
wt=list(int(i) for i in input().split())
val=list(int(i) for i in input().split())
cap=int(input()) # capacity of the knapsack
dp=[[-1 for j in range(cap+1)]for i in range(n+1)]
for i in range(n+1):
    for j in range(cap+1):
        if i==0 or j==0:  # according to the base case we fill first row and column with 0
            dp[i][j]=0
        else:
            dp[i][j]=-1
print(knapsack(wt,val,cap,n,dp))