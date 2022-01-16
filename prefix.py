arr1 =input("Enter string1:")
arr2=input("Enter string2:")
arr=[arr1,arr2]
if not arr:
  print("Longest common prefix:", "")
elif len(arr) == 1:
  print("Longest common prefix:", arr[0])
else:
  arr.sort()
  result = ""
  for i in range(len(arr[0])):
      if arr[0][i] == arr[-1][i]:
          result += arr[0][i]
      else:
          break
  print("Longest common prefix:", result)