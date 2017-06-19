def prodall(myl):
    listlen=len(myl)
    leftl=[None]*listlen
    rightl=[None]*listlen
    resultl=[None]*listlen

    leftl[0]=1

    for i in range(1,listlen):
        leftl[i]=myl[i-1]*leftl[i-1]

    rightl[listlen-1]=1

    for j in range(listlen-2,-1,-1):
        rightl[j]=rightl[j+1]*myl[j+1]

    for k in range(0,listlen):
        resultl[k]=rightl[k]*leftl[k]

    #print(myl, leftl, rightl, resultl)


    return resultl

myl=[1,2,3,4,5]
print(prodall(myl))

