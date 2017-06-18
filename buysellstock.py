# Find the max profit on sale of the stocks from list
# in the list [12,11,15,3,10]
# max profit=10-3=>7 where 3 is purchase price and
# 10 is selling price

# Pseudo code:
# set a pointer at 0th element as purchase price
# set another pointer at 1st element as selling price
# iterate O(n) time complexity to find the best sp-pp difference

def findthemaxprofit(myl):

   minprice=myl[0]
   maxprofit=0

   for price in myl:

       minprice=min(price,minprice)
       comparePrice=price-minprice
       maxprofit=max(maxprofit,comparePrice)


   return maxprofit


stocklist=[12,11,15,3,10]
print(findthemaxprofit(stocklist))

stocklist=[10,12,14,12,13,11,8,7,6,13,23,45,11,10]
print(findthemaxprofit(stocklist))