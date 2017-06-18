# Find the max profit on sale of the stocks from list
# in the list [12,11,15,3,10]
# max profit=10-3=>7 where 3 is purchase price and
# 10 is selling price


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