import numpy as np

# 10. Kiểm tra ma trận vuông xác định dương
def defPosMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không là ma trận vuông ! \n")
    else:
        if np.all(np.linalg.eigvals(mat) > 0):
            print("Ma trận mat xác định dương \n")
            return True
        else:
            print("Ma trận mat không xác định dương \n")
            return False

# 11. Kiểm tra ma trận vuông đối xứng
def symMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    if n_rows != n_cols :
        print("Không là ma trận vuông ! \n")
    else:
        for i in range(n_rows):
            for j in range(n_rows):
                if mat[i,j] != mat[j,i]:
                    return False
        print("Ma trận mat đối xứng")
        return True

# 14. Kiểm tra tính chéo trội của ma trận vuông
def dominantMatrix(mat):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]

    if n_rows != n_cols:
        print("Không là ma trận vuông! Không thể xét tính chéo trội ! \n")
    else:
        diag_A = np.diag(np.abs(mat)) 

        sum_of_row_except_diag_A = np.sum(np.abs(mat), axis = 1) - diag_A 

        sum_of_col_except_diag_A = np.sum(np.abs(mat), axis = 0) - diag_A 

        if np.all(diag_A > sum_of_row_except_diag_A) :
            print("Ma trận mat chéo trội hàng \n")

        elif np.all(diag_A > sum_of_col_except_diag_A):
            print("Ma trận mat chéo trội cột \n")
        else:
            print("Ma trận mat không chéo trội ! \n")