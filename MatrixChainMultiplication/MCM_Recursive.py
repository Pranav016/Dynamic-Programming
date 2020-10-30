# Refer to Aditya Verma MCM ques


# Problem statement- We are given an array of size of matrices. Consecutive pairs of the array form a size of the matrix. 
# For example- arr= 10,20,30
# here matrix sizes can be `10 X 20` or `20 X 30`


# we have to minimize the cost(number of steps/multiplications) to find the product of two or more matrices of the these sizes.

# i starts from 1 since we are using arr[i-1] and arr[i] as our pair

# for recursion we will break `i to k` and then `k+1 to j`

# that is why k will move from i to j-1 because at j=k the 2nd recursive call will be empty or have a single element.


import sys


def mcm(arr,i,j):

    if i>=j:
        return 0
    
    ans=sys.maxsize

    for k in range(i,j):
        ans1=mcm(arr,i,k)
        ans2=mcm(arr,k+1,j)
        ans3=arr[i-1]*arr[k]*arr[j]  # this is the formulae of the cost of multiplication of the matrix in ans1 and ans2
        tempAns=min(ans,ans1+ans2+ans3)
    ans=min(ans,tempAns)
    return ans


# main
n=int(input())
arr=[int(i) for i in input().split()]
print(mcm(arr,1,n-1))