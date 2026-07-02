def setMatrixZeroes(mat):
    n = len(mat)
    m = len(mat[0])

    rows = [False] * n
    cols = [False] * m

    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                rows[i] = True
                cols[j] = True

    
    for i in range(n):
        for j in range(m):
            if rows[i] or cols[j]:
                mat[i][j] = 0



if __name__ == "__main__":
    # Input number of rows and columns
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))

    
    print("Enter the matrix row by row:")
    mat = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print(f"Error: Please enter exactly {m} elements.")
            exit()
        mat.append(row)

    
    setMatrixZeroes(mat)

    
    print("\nMatrix after setting zeroes:")
    for row in mat:
        print(*row)