# #cau a
# def tinh_tong(n):
#     tong = 0  # Khởi tạo tổng
#     for i in range(1, n+1):  # Lặp từ i = 1 đến i = n
#         tong += 1 / (i * (i + 1))  # Công thức tính tổng
#     return tong

# # Vòng lặp kiểm tra điều kiện nhập
# while True:
#     try:
#         n = int(input("Nhập vào số nguyên dương: "))  # Nhập và chuyển đổi thành số nguyên
#         if n > 0:  # Kiểm tra n > 0
#             break  # Thoát khỏi vòng lặp nếu nhập đúng
#         else:
#             print("Nhập sai! Vui lòng nhập lại (n > 0).")
#     except ValueError:
#         print("Nhập sai! Vui lòng nhập một số nguyên dương.")

# # Gọi hàm tính tổng và in kết quả
# ket_qua = tinh_tong(n)
# print(f"Tổng là: {ket_qua}")

# #  #câu b
# def ting_tong(n):
#     tong =0
#     for i in range(4, n+1):
#         tong+= (i+1) / (i-1)
        
#         return tong
# while True:
#     try:
#         n = int(input("Nhập vào số nguyên dương: "))  # Nhập và chuyển đổi thành số nguyên
#         if n >= 4:  # Kiểm tra n > 0
#             break  # Thoát khỏi vòng lặp nếu nhập đúng
#         else:
#             print("Nhập sai! Vui lòng nhập lại (n > 0).")
#     except ValueError:
#         print("Nhập sai! Vui lòng nhập một số nguyên dương.")
# ket_qua =ting_tong(n)
# print(f"tong : {ket_qua}")
# #caau c

# def tinh_tong_1(n):
#     tong=4
#     for i in  range(4, n+1):
#         tong+=(i+1)/(i-1)
#         return tong
# def tinh_tong_2(n):
#     tong=1
#     for i in range(1, n+1):
#         tong+=i/(i+1)
#         return tong    
# while True:
#     try:
#         n= int(input("nhap vao so nguyen duong:"))
#         if n >=4 or n>=1 :
#             break
#         else:
#             print("vui long nhap lai")
#     except ValueError:    
#         print("nhap sai")
# ket_qua=tinh_tong_1(n)+tinh_tong_2(n)
# print(f"ket_qua(n): {ket_qua}")       
# #câu d
# def tinh_tong_d(n):
#     tu_so = sum(
#         sum(i / (j + 1) for j in range(1, i + 1))
#         for i in range(4, n + 1)
#     )
#     # Tính mẫu số
#     mau_so = n + 5
    
#     # Trả về kết quả
#     return tu_so / mau_so
# while True:
#     try:
#         n= int(input("nhap vao so nguyen duong"))
#         if n>4:
#             break
#         else:
#             print("vui long nhap so dung")
#     except ValueError:
#         print("nhap sai")
# ket_qua=tinh_tong_d(n)
# print(f"tong: {ket_qua}")
#câu e
# def tinh_tich(n):
#     tich = 1
#     for i in range(1, n+1):
#         tich*= (n+1)
#     return tich
# while True:
#     try:
#         n = int(input("nhap vao so nguyen duong"))
#         if n >0:
#             break
#         else:
#             print("nhap vao so lon hon 0")
#     except ValueError:
#         print("nhap sai")

# ket_qua= tinh_tich(n)
# print(f"tinh tich : {ket_qua}")        
#câu f
# def tich_tu(n):
#     tich = 1
#     for i in range(2, n+1):
#         tich *= (i-1)
#     return tich
# def tich_mau(n):
#     tich = 1
#     for j in range(4, n+1):
#         tich *= 1/j    
#     return tich
# while True:
#     n= int(input("nhap vao so nguyen duong"))
#     try:
#         if n>=2 and n >=4:
#             break
#         else:
#             print("vui long nhap so dung yeu cau")
#     except ValueError:
#         print("nhap sai")        
    
# ket_qua=tich_tu(n)/tich_mau(n)
# print(f"ket qua : {ket_qua}")
#câu g
def tinh_tong(n):
    tong =1
    for i in range(8, n+1):
        tich += (i*i)/tich_mau(n)
    return tong   
def  tich_mau(n):
    tich = 1
    for j in range(4, n+1):
        tich *= 1/j
    return tich
n= int(input("nhap vao"))
ket_qua=tinh_tong(n)
print(f"ket qua {ket_qua}")