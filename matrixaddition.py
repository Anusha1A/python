if __name__ == '__main__':
	rows = int(input("Enter the Number of rows : " ))
	columns= int(input("Enter the Number of Columns: "))
	print("matrix1")
	matrix1= [[int(input()) for i in range(columns)] for i in range(rows)]
	for a in matrix1: 
		print(a)
	print("matrix2")
	matrix2= [[int(input()) for i in range(columns)] for i in range(rows)]
	for b in matrix2: 
		print(b)
	res=[[0 for i in range(columns)] for i in range(rows)]
	for i in range(rows):
   		 for j in range(columns):
       			 res[i][j] = matrix1[i][j]+matrix2[i][j]

	print("Matrix addition ")
	for c in res:
  		 print(c)