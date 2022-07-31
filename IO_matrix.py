def ioMatrix():
    n_rows = int(input("Nhập số hàng: "))
    n_cols = int(input("Nhập số cột: "))
 
    mat = []

    for i in range(n_rows):		 
        a = []
        for j in range(n_cols):	
            a.append(float(input()))
        mat.append(a)

    for i in range(n_rows):
        for j in range(n_cols):
            print(mat[i][j], end = " ")
        print()

    return mat
