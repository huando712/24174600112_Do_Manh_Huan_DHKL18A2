#yêu cầu về nhà
#Thực hiện các phép tính cơ bản của ma trận với số và của ma trận với ma trận
#xử lý ma trận
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

print(matrix_a)
#cộng hai ma trận
ma_tran_a = [[0, 5, 8],
             [8, 6, 9],
             [1, 1, 2],]

ma_tran_b = [[0, 7, 1],
             [8, 6, 5],
             [1, 2, 2],]
ket_qua = [[0, 0, 0],
           [0, 0, 0],            
           [0, 0, 0],]     
for h in range(len(ma_tran_a)):
    for c in range(len(ma_tran_a[0])):
        ket_qua[h][c] = ma_tran_a[h][c] + ma_tran_b[h][c]
    
print(f"nhan hai ma tran: {ket_qua}")

#trừ 2 ma trận
ma_tran_1 = [[2, 4, 5, 6],
             [3, 5, 6, 1],
             [4, 9, 0, 3],
             [2, 2, 8, 6],]
ma_tran_2 =  [[2, 4, 5, 6],
              [5, 4, 6, 1],
              [4, 7, 0, 3],
              [1, 2, 8, 6],]            