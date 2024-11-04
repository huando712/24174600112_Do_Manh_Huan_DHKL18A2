# Nhập hai số từ người dùng
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))


while b != 0:
    a, b = b, a % b

# In ra ước chung lớn nhất
print(f"Ước chung lớn nhất của hai số là: {a}")
