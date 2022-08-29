for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
print("*******************************")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print("\r")
print("******************")

b=0
for i in range(5,0,-1):
    b+=1
    for j in range(1,i+1):
        print(3,end="")
    print("\r")