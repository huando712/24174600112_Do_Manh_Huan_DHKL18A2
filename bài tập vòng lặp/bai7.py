# Nhập vào n
n = int(input("Nhập vào một số nguyên dương n: "))
# Duyệt qua từng số từ 2 đến n - 1
for n in range(2, n):
    is_prime = True  # Giả sử num là số nguyên tố

    # Kiểm tra từ 2 đến num - 1
    for i in range(2, n):
        if n % i == 0:  # Nếu tìm thấy ước số thì không phải số nguyên tố
            is_prime = False
            break

    # Nếu là số nguyên tố, in ra màn hình
    if is_prime:
        print(n, end=" ")
print(f"Các số nguyên tố nhỏ hơn {n} là:", end=" ")