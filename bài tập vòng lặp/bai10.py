# Nhập hai số bất kỳ
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Xác định giá trị nhỏ nhất giữa hai
# Xác định giá trị nhỏ nhất giữa hai số để tối ưu vòng lặp
nho_nhat = min(abs(a), abs(b))  # Lấy giá trị tuyệt đối để tránh số âm

# Tìm ước chung lớn nhất (UCLN) bằng cách duyệt ngược từ giá trị nhỏ nhất về 1
ucln = 1
for i in range(nho_nhat, 0, -1):
    if a % i == 0 and b % i == 0:
        ucln = i
        break

# In ra kết quả UCLN
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
