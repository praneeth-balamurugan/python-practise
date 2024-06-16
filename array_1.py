from array import *
# vals= array('i',(1,23,4,56,7))

# vals=array('i',sorted(vals))
# print(vals[2])

# for i in range(len(vals)):
#      print (vals[i])


size=int(input("enter size"))
arr=array('i',[])

for i in range(size):
      value=int(input())
      arr.append(value)


arr=array('i',sorted(arr))
max2=arr[size-2]
print("Array")
for i in range(size):
      print(arr[i])


print("max",max2)
x=0
for i in arr:
      if(i==max2):
             x+=1


print(x)
        