def solution(X, A):
    positions =[]

    for time in range(len(A)):
        position = A[time]

        if position not in positions: #add positions if not already in the list
            positions.append(position)
        
        if len(positions) == X: #Checks if all positions are covered
            return time
            
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4])) #Prints 6