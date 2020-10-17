# Probem statement- We are given an array of integers and we have to check if there any subset possible in the given array whose sum comes out to be equal to the sum in the question.


def subsetSum(arr,n,sum,dp):

    for i in range(1,n+1): # we start from 1 because 0th rows and columns have already been initialized
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                includeNo=dp[i-1][j-arr[i-1]]
                notIncludeNo=dp[i-1][j]
                dp[i][j]=includeNo or notIncludeNo
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][sum]



# main
n=int(input())
arr=[int(i) for i in input().split()]
sum=int(input())
dp=[[-1 for j in range(sum+1)]for i in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if i==0:
            dp[i][j]=False
        if j==0:
            dp[i][j]=True
        
print(subsetSum(arr,n,sum,dp))