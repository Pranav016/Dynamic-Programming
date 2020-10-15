# logical intiution for this problem is that if the wt. comes under the capacity then we can either choose to add it to our bag or choose to not add it to our bag.
# if it is outside the capacity of the bag/knapsack then it becomes obvious that we will not consider it.


def knapsack(wt,val,cap,n):
    if n==0 or cap==0:
        return 0
    
    if wt[n-1]<=cap:
        includeThisWt = val[n-1] + knapsack(wt,val,cap-wt[n-1],n-1)
        notIncludeThisWt = knapsack(wt,val,cap,n-1)
        return max(includeThisWt , notIncludeThisWt)
    else:
        return knapsack(wt,val,cap,n-1)


# main
n=int(input()) # size of the array
wt=list(int(i) for i in input().split())
val=list(int(i) for i in input().split())
cap=int(input()) # capacity of the knapsack
print(knapsack(wt,val,cap,n))