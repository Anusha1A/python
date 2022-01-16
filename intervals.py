def mergeInterval2(arr, n, newPair) :
	stk = []
	stk.append(arr[0])
	top = stk[len(stk) - 1]
	if (newPair[0] < top[1]) :
		stk.pop()
		top[0] = min(top[0], newPair[0])
		top[1] = max(top[1], newPair[1])
		stk.append(top)

	else :
		stk.append(newPair)
	for i in range(1, n) :
		top = stk[len(stk) - 1]
		if (arr[i][0] < top[1]):
			stk.pop()
			top[0] = min(top[0], arr[i][0])
			top[1] = max(top[1], arr[i][1])
			stk.append(top)
		
		else :
			stk.append(arr[i])
	finalIntervals = []
	while (len(stk) > 0) :
	
		ele = stk[len(stk) - 1]
		stk.pop()
		finalIntervals.append(ele)
	while (len(finalIntervals) > 0) :
	
		ele = finalIntervals[len(finalIntervals) - 1]
		finalIntervals.pop()
		
		print(ele[0] , end = ", ")
		print(ele[1])
arr2 = [ [ 1, 2 ], [ 3, 5 ], [ 6, 7 ], [ 8, 10 ], [ 12, 16 ] ]
newPair = [ 4, 9 ]
n2 = len(arr2)
mergeInterval2(arr2, n2, newPair)

