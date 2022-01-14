if __name__ == '__main__':
	rows = int(input("Enter the Number of rows : " ))
	columns= int(input("Enter the Number of Columns: "))
	print("matrix1")
	matrix1=[[int(input()) for i in range(columns)] for i in range(rows)]
	print("given matrix")
	for a in matrix1: 
		print(a)

	result=[[0 for i in range(columns)] for i in range(rows)]

	for i in range(rows):
  
   		for j in range(columns):
     			  result[j][i] = matrix1[i][j]
	print("Transpose matrix")
	for r in result:
  	                   	print(r)