# Nhập hai số bất kỳ
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tìm ước chung lớn nhất (UCLN) bằng cách duyệt từ nhỏ nhất đến 1
ucln = 1
nho_nhat = min(abs(a), abs(b))  # Lấy giá trị tuyệt đối để tránh số âm

for i in range(nho_nhat, 0, -1):
    if a % i == 0 and b % i == 0:
        ucln = i
        break

# Tính bội chung nhỏ nhất (BCNN) dựa vào UCLN
bcnn = abs(a * b) // ucln

# In ra kết quả
print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn}")
