import numpy as np

from IO_matrix import *

# 12. Giá trị riêng, vector riêng 

def eigen(mat):
    eigen_value, eigen_vector = np.linalg.eig(mat)

    eigen_vector = eigen_vector.T

    # giá trị riêng
    print("Giá trị riêng : \n ", eigen_value)

    # vector riêng
    for i in range(eigen_vector.shape[0]):
        print("Vector riêng ứng với trị riêng {0} là : {1}".format(eigen_value[i], eigen_vector[i]))
