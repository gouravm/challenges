def uniq(str):
    l=[]

    for c in str:
        if c not in l:
            l.append(c)

    print(l)
    return "".join(l)


str="tree traversal"
print(uniq(str))