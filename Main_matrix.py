from File_matrix import *
from IO_matrix import *
from Basic_operator_matrix import *
from Basic_matrix import *
from Check_matrix import *
from Decomposition_matrix import *
from Find_matrix import *
from Eigen_matrix import *
from Library_io_matrix import *
from Library_file_matrix import *

# main
# ============================================================================
while True:
    print("_" * 80 + "\n")
    print("\t" * 2 + "CHÀO MỪNG CÁC BẠN ĐẾN VỚI THƯ VIỆN VỀ MA TRẬN" + "\t" * 5)
    print("_" * 80 + "\n")

    print("\nChọn 1 để nhập ma trận từ bàn phím \n")
    print("Chọn 2 để nhập ma trận từ file \n")

    select = int(input())

    if select == 1:
        libraryIOMatrix()

    if select == 2:
        libraryFileMatrix()
