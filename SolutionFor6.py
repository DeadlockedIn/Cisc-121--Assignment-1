def solution(A): 
 for number in range(1, len(A) + 1): #Checks for number in the range
  if number not in A: #If not in A, then return it as 0(missing)
   return 0

 return 1

print(solution([4, 1, 3, 2])) #Prints 1