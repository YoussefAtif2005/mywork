# Question 1
l=[2, 5, 7]
n=len(l)
M=1
for i in range(0, n):
    M=M*l[i]



print("La multiplication de l =",M)    

# Question 2
lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]



# Question 3 (Help of ChatGpt )
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for key in d1.keys():
    d[key]=d1[key]

for key in d2.keys():
    if key in d.keys():
        d[key]+=d2[key]
    else:
        d[key]=d2[key]  
        
print(d)         




# Question 4
import math
dictn={}
a=int(input("Write your number: "))
ca=a*a
rca=math.sqrt(ca)
rca=int(rca)
for i in range(1, rca+1):
    dictn[i]=i*i

print(dictn)    

# Question 6
set={"shmg", "lhg"}
set.add("klshf")
set.remove("shmg")
print(set)


    

