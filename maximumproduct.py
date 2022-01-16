def maxProduct(arr, n): 
	if n < 3:
        		return -1
	arr.sort()
	print("Maximum product array is:")
	print(arr[n-1]*arr[n-2]*arr[n-3])
	return
arr=[]
n=int(input("Enter size of an array"))
for i in range(0,n):
	a=int(input())
	arr.append(a)
maxProduct(arr, n) 


