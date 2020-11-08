# Fractional knapsack greedy/ recursive approach


class ItemValue:
    def __init__(self,wt,val):
        self.wt=wt
        self.val=val
        self.cost=val//wt

    def __lt__(self,other): # overloading the less than operator
        return self.cost<other.cost

class FractionalKnapsack:
    def getMaxValue(self,wt,val,capacity):
        totalValue=0
        itemList=[]
        for i in range(len(wt)):
            itemList.append(ItemValue(wt[i],val[i])) # appending ItemValue objects into the list
            i+=1
        itemList.sort(reverse=True) # sorting in descending order
        for obj in itemList:
            if capacity-obj.wt>=0:
                capacity=capacity-obj.wt
                totalValue=totalValue + obj.val
            else:
                fraction=capacity/obj.wt
                resultantValue=obj.val*fraction
                totalValue=totalValue+resultantValue
                capacity=int(capacity-(obj.wt*fraction))
                break
        return totalValue


# main
wt=[int(i) for i in input().split()]
val=[int(i) for i in input().split()]
capacity=int(input())
obj=FractionalKnapsack()
maxValue=obj.getMaxValue(wt,val,capacity)
print(maxValue)