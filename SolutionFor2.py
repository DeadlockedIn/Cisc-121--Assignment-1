def solution(A):
    for number in A:
        count = A.count(number) #Counts how many times that number appears in A
        if count % 2 == 1: #Checks if the count is odd
            return number

print(solution([9, 3, 9, 3, 9, 7, 9])) #Prints 7