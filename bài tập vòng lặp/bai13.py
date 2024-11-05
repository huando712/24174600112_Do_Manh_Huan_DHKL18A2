# Nhập số từ người dùng
n = int(input("Nhập vào một số: "))

# Kiểm tra số lớn hơn 1
if n > 1:
    u = 2
    print("Các thừa số nguyên tố là:", end=" ")

    # Tìm các thừa số nguyên tố và in trực tiếp
    while n > 1:
        if n % u == 0:
            print(u, end=" ")
            n = n // u  # Chia n cho divisor
        else:
            u=u+ 1  # Tăng divisor lên 1
else:
    print("Vui lòng nhập một số lớn hơn 1.")

