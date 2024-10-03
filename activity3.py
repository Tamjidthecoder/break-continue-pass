a=10
for i in range(11):
    if i>0:
       a=a-1
       if a==5:
           continue
    print(i)
print("THIS IS OUTSIDE FORLOOP")
