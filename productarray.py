def productArray(A, n):
	if(n == 1):
		return 0
	left = [0]*n
	right = [0]*n
	prod = [0]*n
	left[0] = 1
	right[n - 1] = 1
	for i in range(1, n):
		left[i] = A[i - 1] * left[i - 1]
	for j in range(n-2, -1, -1):
		right[j] = A[j + 1] * right[j + 1]
	for i in range(n):
		prod[i] = left[i] * right[i]
	for i in range(n):
		print("{}".format(prod[i]), end =' ')
if __name__ == '__main__':
	A = [1,2,3,4,5]
	n = len(A)
	print("B:")
	productArray(A, n)

