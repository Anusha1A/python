if __name__ == '__main__':
	rows = int(input("Enter the Number of rows : " ))
	columns = int(input("Enter the Number of columns : " ))
	rows1 =int(input("Enter the Number of rows: "))
	columns1 = int(input("Enter the Number of columns : " ))
	print("matrix1")
	matrix1= [[int(input()) for i in range(columns)] for j in range(rows)]
	for a in matrix1: 
		print(a)
	print("matrix2")
	matrix2= [[int(input()) for i in range(columns1)] for j in range(rows1)]
	for b in matrix2: 
		print(b)
	res=[[0 for i in range(columns1)] for i in range(rows)]
	for i in range(rows): 
   		for j in range(columns): 
        			for k in range(columns1): 
          				res[i][k] += matrix1[i][j] * matrix2[j][k] 
	print("The Resultant Matrix Is ::>")
	for r in res: 
   		print(r) 