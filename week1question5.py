def sqsum():
    sum=0
    Arr=list(map(int,input().split(",")))
    for i in range(len(Arr)):
        sum = sum + Arr[i]**2
    return sum
sumarray=sqsum()
print(sumarray)