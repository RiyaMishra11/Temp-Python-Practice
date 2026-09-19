# Day 11 - 43: Matrix Algorithms

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# 1. Print matrix
print("1. Matrix:")
for row in matrix: print(row)

# 2. Sum elements
print("2. Sum:", sum(map(sum, matrix)))

# 3. Row sums
print("3. Row sums:", [sum(row) for row in matrix])

# 4. Column sums
print("4. Column sums:", [sum(matrix[r][c] for r in range(3)) for c in range(3)])

# 5. Main diagonal
print("5. Main diagonal:", [matrix[i][i] for i in range(3)])

# 6. Transpose
print("6. Transpose:", [list(row) for row in zip(*matrix)])

# 7. Rotate 90 degrees clockwise
print("7. Rotated:", [list(row) for row in zip(*matrix[::-1])])

# 8. Maximum element
print("8. Maximum:", max(map(max, matrix)))

# 9. Search element
target = 6
print("9. Search 6:", any(target in row for row in matrix))

# 10. Spiral traversal
top, bottom, left, right = 0, 2, 0, 2
spiral = []
while top <= bottom and left <= right:
    spiral += matrix[top][left:right+1]; top += 1
    for r in range(top, bottom+1): spiral.append(matrix[r][right])
    right -= 1
    if top <= bottom:
        spiral += matrix[bottom][left:right+1][::-1]; bottom -= 1
    if left <= right:
        for r in range(bottom, top-1, -1): spiral.append(matrix[r][left])
        left += 1
print("10. Spiral:", spiral)
