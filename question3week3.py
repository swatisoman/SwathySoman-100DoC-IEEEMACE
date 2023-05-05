#Write a program that stores numbers entered by the user into a file. Then once the user stops, another function must sort through the file and create a new file which separates the numbers into 3 groups, even, odd and prime
def sortfile(lst):
    even=[]
    odd=[]
    prime=[]
    for i in range(len(lst)):
        if lst[i]%2==0:
            even.append(lst[i])
        if lst[i]%2!=0:
            odd.append(lst[i])
        m=0
        if lst[i]==0:
            m=1
        for j in range(2,lst[i]//2 + 1):
            if(lst[i]%j==0):
                m=m+1
                break
        if m==0:
            prime.append(lst[i])
    f=open("sortedfile.txt","w")
    f.write("Output File Even : {0} Odd : {1} Prime : {2}".format(even,odd,prime))
    f.close()
    fp=open("sortedfile.txt","r")
    fp.seek(0)
    print("Outputfile: ")
    output=fp.read()
    print(output)
    fp.close()

f=open("number.txt","w")
print("Input File ")
numbers=list(map(int,input().split(" ")))
num=str(numbers)
f.write(num)
f.close()
sortfile(numbers)


