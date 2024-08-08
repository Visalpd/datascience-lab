ar=[]
n=int(input("enter number of elements:"))
print("enter the elements")
for i in range(0,n):
	x=int(input())
	ar.append(x)
print(ar)
for i in range(0,n):
	for j in range(i+1,n):
		if ar[i]>ar[j]:
			temp=ar[i]
			ar[i]=ar[j]
			ar[j]=temp
print("the sorted array are :",ar)
