import numpy as np

# 6. Kích thước của ma trận
def shapeMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    print("Ma trận mat có kích thước {0} x {1} \n".format(n_rows, n_cols))

# 7. Tìm hạng của ma trận 
def rankMatrix(mat):
    return np.linalg.matrix_rank(mat)

# 8. Chuyển vị của ma trận 
def transMatrix(mat):
    return mat.T

# 9. Ma trận đặc biệt

# 9.1 Ma trận đơn vị của ma trận vuông
def idMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.eye(n_rows)

# 9.2 Ma trận tam giác trên của ma trận vuông
def upperMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.triu(mat)   

# 9.3 Ma trận tam giác dưới của ma trận vuông
def lowerMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.tril(mat)   

# 9.4 Ma trận đường chéo của ma trận vuông
def diagMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không là ma trận vuông ! \n")
    else:
        return np.diag(np.diag(mat))


