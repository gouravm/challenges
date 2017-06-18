# Find the max profit on sale of the stocks from list
# in the list [12,11,15,3,10]
# max profit=10-3=>7 where 3 is purchase price and
# 10 is selling price

# Pseudo code:
# set a pointer at 0th element as purchase price
# set another pointer at 1st element as selling price
# iterate O(n) time complexity to find the best sp-pp difference

def findthemaxprofit(myl):
    maxprofit=0

    #purchase price pointer
    pppointer=0

    #selling price pointer
    sppointer=pppointer+1

    #len of array
    end=len(myl)

    profit=0
    while sppointer<end:
        profit=myl[sppointer]-myl[pppointer]
        if profit>maxprofit:
            maxprofit=profit
        pppointer+=1
        sppointer+=1

    return maxprofit


stocklist=[12,11,15,3,10]
print(findthemaxprofit(stocklist))
