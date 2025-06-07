a = [[1,1,6,6],
     [2,3,1,7],
     [3,5,4,8],
     [4,16,5,9]]

def det_loop(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det_value = 0
    for j in range(0, len(matrix)):
        cofator = (-1) ** (0 + j) * matrix[0][j] * det_loop([row[:j] + row[j+1:] for row in matrix[1:]])
        det_value += cofator
        
    return det_value
        
print(det_loop(a))