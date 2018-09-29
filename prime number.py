import math

print("pls enter a number:")
num1=int(input())
n=1
i=1
j=0
test1=1
for n in range(2,num1):
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            j=j+1
    if(j==1):
        print(n)
        j=0
    else: j=0


    










