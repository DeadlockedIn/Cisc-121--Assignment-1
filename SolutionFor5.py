def solution(A):
    best = abs(A[0] - sum(A[1:])) #The difference for the first split

    for split in range(1, len(A)): #Loops every split
        left = sum(A[:split]) #Before split
        right = sum(A[split:]) #After split
        difference = abs(left - right)

        if difference < best: #Save the smallest difference
            best = difference
    
    return best

print(solution([3, 1, 2, 4, 3])) #Prints 1