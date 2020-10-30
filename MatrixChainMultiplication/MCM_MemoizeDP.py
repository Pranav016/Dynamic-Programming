
import sys


def mcm(arr,i,j,dp):

    if i>=j:
        return 0
    
    if dp[i][j]!=0:
        return dp[i][j]

    ans=sys.maxsize

    for k in range(i,j):
        ans1=mcm(arr,i,k,dp)
        ans2=mcm(arr,k+1,j,dp)
        ans3=arr[i-1]*arr[k]*arr[j]
        tempAns=min(ans,ans1+ans2+ans3)
    ans=min(ans,tempAns)
    dp[i][j]=ans
    return ans


# main
n=int(input())
arr=[int(i) for i in input().split()]
dp=[[-1 for j in range(n+1)]for i in range(n+1)]
print(mcm(arr,1,n-1,dp))