a="12,23,1,24,124"

temp=a.split(",")
last=[]
for i in range(len(temp)):
    last.append(int(temp[i]))
print(last)