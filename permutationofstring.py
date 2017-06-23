def checkperm(str1,str2):

    if sorted(str1)==sorted(str2):
        return True
    else:
        return False


def checkpermlen(str1,str2):
    if len(str1)!=len(str2):
        return False
    mdict={}
    count=1

    for c in str1:
        if c not in mdict:
            mdict[c]=count
        else:
            mdict[c]+=1
    print (mdict)

    for c in str2:
        if c in mdict:
            mdict[c]-=1
            if mdict[c]==0:
                mdict.pop(c)

    print(mdict,len(mdict))

    if (len(mdict)>0):
        return False
    else:
        return True


str1="great"
str2="targt"
print(checkperm(str1,str2))
print(checkpermlen(str1,str2))