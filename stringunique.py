def checkunique(str):
    mdict={}
    count=1

    for c in str:
        if c not in mdict:
            mdict[c]=count
        else:
            mdict[c]+=1

    print(mdict)

    for k,v in mdict.items():
        if v>1:
            return False

    return True

def strunique(str):
    s=set()

    for c in str:
        if c in s:
            print(list(s))
            return False
        else:
            s.add(c)

    print(list(s))

    return True


str="cassandra"
print(checkunique(str))
print(strunique(str))
