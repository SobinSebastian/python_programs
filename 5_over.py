n=int(input("Enter the number of elements:"))
li=[]
for i in range(n):
    v=int(input("Enter a integer value :\n\t"))
    if(v<=100):
        li.append(v)
    elif(v>100):
        li.append("Over")
print(li)