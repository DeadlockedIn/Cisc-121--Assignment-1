def solution(A):
    for number in range(1, len(A) + 2): #Checks for number in the range
     if number not in A: #Checks if the current number isn't in A
      return number

print(solution([2, 3, 1, 5])) #Prints 4