alpha=input()
out=[]
s=""
for i in range(len(alpha)):
    if(alpha[i]==" "):
        continue
    elif(int(ord(alpha[i]))<91 and int(ord(alpha[i]))>64):
        out.append(int(ord(alpha[i])-64))
    elif(int(ord(alpha[i]))<123 and int(ord(alpha[i])>96)):
        out.append(int(ord(alpha[i])-96))
    else:
        continue
for j in range(len(out)):
    s = s + str(out[j]) + " "
print(s)



