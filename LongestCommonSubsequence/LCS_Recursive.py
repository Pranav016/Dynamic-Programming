# Problem Statement- Given two strings, print the lenght of the longest common subsequence for the two given strings.

# Difference between substring and subsequence-   Substring is continous whereas subsequence may or may not be a continous string.


def lcs(a,b,n,m,ans):
    if n==0 or m==0:
        return 0

    if a[n-1]==b[m-1]:
        ans=1+lcs(a,b,n-1,m-1,ans)
    else:
        ans1=lcs(a,b,n-1,m,ans)
        ans2=lcs(a,b,n,m-1,ans)
        ans=max(ans1,ans2)
    return ans



# main
a=str(input())
n=len(a)
b=str(input())
m=len(b)
print(lcs(a,b,n,m,0))