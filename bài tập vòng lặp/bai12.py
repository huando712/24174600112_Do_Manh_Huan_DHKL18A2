# Nhập tử số và mẫu số
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

# Kiểm tra mẫu số khác 0
if mau_so == 0:
    print("Mẫu số phải khác 0.")
else:
    # Xác định giá trị nhỏ nhất giữa tử số và mẫu số
    nho_nhat = min(abs(tu_so), abs(mau_so))  # Lấy giá trị tuyệt đối để tránh số âm

    # Tìm ước chung lớn nhất (UCLN) bằng cách duyệt ngược từ nhỏ nhất đến 1
    ucln = 1
    for i in range(nho_nhat, 0, -1):
        if tu_so % i == 0 and mau_so % i == 0:
            ucln = i
            break

    # Rút gọn tử số và mẫu số
    tu_so = tu_so // ucln
    mau_so = mau_so // ucln
    
    # In ra phân số tối giản
    print(f"Phân số tối giản là: {tu_so}/{mau_so}")

