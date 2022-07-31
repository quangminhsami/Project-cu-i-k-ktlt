import numpy as np

# 1. Cộng 2 ma trận
def addMatrix(mat1, mat2):
    n1_rows = mat1.shape[0]
    n2_rows = mat2.shape[0]
    n1_cols = mat1.shape[1]
    n2_cols = mat2.shape[1]

    if n1_rows != n2_rows or n1_cols != n2_cols:
        print("Không thể cộng 2 ma trận! \n")
    else:
        return mat1 + mat2 

# 2. Trừ 2 ma trận
def subMatrix(mat1, mat2):
    n1_rows = mat1.shape[0]
    n2_rows = mat2.shape[0]
    n1_cols = mat1.shape[1]
    n2_cols = mat2.shape[1]

    if n1_rows != n2_rows or n1_cols != n2_cols:
        print("Không thể trừ 2 ma trận! \n")
    else:
        return mat1 - mat2

# 3. Nhân 2 ma trận
def mulMatrix(mat1, mat2):
    n1_rows = mat1.shape[0]
    n2_rows = mat2.shape[0]
    n1_cols = mat1.shape[1]
    n2_cols = mat2.shape[1]

    if n1_cols != n2_rows or n1_rows != n2_cols:
        print("Không thể nhân 2 ma trận! \n")
    else:
        return mat1 @ mat2

# 4. Tính định thức của ma trận vuông 
# 4.1 Tự lập trình
def detMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không phải ma trận vuông !, không thể tính định thức \n")
    else:
        count = 0
        B = np.arange(n_rows ** 2)
        B = B.reshape((n_rows,n_rows))
        B = np.zeros_like(B, dtype = float)
        
        for i in range(n_rows): 
            for j in range(n_cols):
                B[i,j] = mat[i,j]
        
        for k in range(n_rows):
            i_max = k
            v_max = abs(B[i_max, k])
            for i in range(k+1, n_rows):
                if B[i,k] > v_max:
                    v_max = abs(B[i,k])
                    i_max = i

            if i_max != k:
                for i in range(n_rows):
                    temp = B[i_max, i]
                    B[i_max, i] = B[k,i]
                    B[k,i] = temp
                count += 1

            for i in range(k+1, n_rows):
                f = B[i,k] / B[k,k]
                for j in range(k+1,n_cols):
                    B[i,j] -= B[k,j] * f
                B[i,k] = 0

        det = -1 ** count 
        for i in range(n_rows):
            det *= B[i,i]

        return det 
            
# 4.2 Dùng thứ viện Numpy
def detNumpyMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không phải ma trận vuông !, không thể tính định thức \n")
    else:
        return np.linalg.det(mat)

# 13. Tính chuẩn của ma trận

# 13.1 Chuẩn 1
def norm1Matrix(mat):
    return np.linalg.norm(mat, 1)

# 13.2 Chuẩn 2
def norm2Matrix(mat):
    return np.linalg.norm(mat, 2)

# 13.3 Chuẩn vô cùng
def normInfMatrix(mat):
    return np.linalg.norm(mat, np.inf)
