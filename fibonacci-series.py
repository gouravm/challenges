def fibrecur(n):
    if n==1:
        return n
    return n * fibrecur(n-1)

def fibnonrecur(num):
    if num==1:
        return n
    sum=1
    for i in range(num,0,-1):
        sum=sum*i

    return sum


n=5
print(fibrecur(n))
print(fibnonrecur(n))