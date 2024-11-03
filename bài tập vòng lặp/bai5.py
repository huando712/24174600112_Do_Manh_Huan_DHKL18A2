# Nhập số từ người dùng
n = int(input("Nhập một số nguyên: "))

# Kiểm tra số hoàn hảo
if n < 1:
    print(f"{n} không phải là số hoàn hảo.")
else:
    tong = 0  # Khởi tạo biến tổng các ước số

    # Tính tổng các ước số dương của number
    for i in range(1, n):
        if n % i == 0:  # Nếu i là ước số
            tong =tong + i

    # So sánh tổng các ước số với số ban đầu
    if tong== n:
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo.")
