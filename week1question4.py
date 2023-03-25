def sumarr():
    sum=0
    Arr=list(map(int,input().split(",")))
    for i in range(len(Arr)):
        sum=sum+Arr[i]
    return sum
sumarray=sumarr()
print(sumarray)