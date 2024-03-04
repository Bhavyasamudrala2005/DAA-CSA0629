def generate_pascals_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(n - 1)
        row = [1]
        for i in range(1, n - 1):
            row.append(triangle[n - 2][i - 1] + triangle[n - 2][i])
        row.append(1)
        triangle.append(row)
        return triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))
rows = 5
print("Pascal's Triangle:")
triangle = generate_pascals_triangle(rows)
print_pascals_triangle(triangle)
