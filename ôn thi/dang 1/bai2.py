# Bài 2: Nhập số nguyên dương n và tính tổng n số nguyên dương chẵn liên tiếp
def tinh_tong_chan(n):
    tong = 0
    so_chan = 2
    for _ in range(n):
        tong += so_chan
        so_chan += 2
    return tong

# Nhập số nguyên dương n
while True:
    n = input("Nhập số nguyên dương n: ")
    try:
        # Kiểm tra điều kiện input
        if  n.isdigit and int(n) > 0:
            n = int(n)
            break
        else:
            print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    except :
        print("Đã xảy ra lỗi:")

# Tính tổng và in kết quả
ket_qua = tinh_tong_chan(n)
print("Tổng n số chẵn liên tiếp là:", ket_qua)

# Bài 3: Nhập số nguyên dương n và tính tích n số nguyên dương lẻ liên tiếp
def tinh_tich_le(n):
    tich = 1 #số lẻlẻ
    so_le = 1
    for _ in range(n):
        tich *= so_le
        so_le += 2 #mỗi lần tăng thêm 2 đơn vị
    return tich

# Kiểm tra input bằng vòng lặp while
while True:
    n = input("Nhập số nguyên dương n: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break  # Thoát khỏi vòng lặp khi input hợp lệ
    else:
        print("Vui lòng nhập một số nguyên dương hợp lệ.")

# Tính tích và in kết quả
ket_qua = tinh_tich_le(n)
print("Tích n số lẻ liên tiếp là:", ket_qua)
#Bài 4: Nhập số nguyên dương n và tính n!
def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):  # Tính giai thừa từ 1 đến n
        giai_thua *= i
    return giai_thua

while True:
    try:
        n = input("Nhập vào số nguyên dương: ")
        if n.isdigit() and int(n) > 0:  # Kiểm tra n là số nguyên dương
            n = int(n)
            break
        else:
            print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    except :
        print("Đã xảy ra lỗi:")

print(f"{n}! = {tinh_giai_thua(n)}")


            


    