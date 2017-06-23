def strcomp(mstr):
    count=0
    strlen=len(mstr)
    newstr=""

    for c in range(0,strlen):
        count+=1
        if c+1>=strlen or mstr[c] != mstr[c+1]:
            newstr+=mstr[c]+str(count)
            count=0

    return newstr

mstr="aabbccccd"
print(mstr,strcomp(mstr))