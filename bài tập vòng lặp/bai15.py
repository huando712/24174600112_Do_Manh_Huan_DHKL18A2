# Nhập số ở hệ cơ số 10
decimal_number = int(input("Nhập số ở hệ cơ số 10: "))

# Kiểm tra trường hợp đặc biệt nếu số là 0
if decimal_number == 0:
    print("Số ở hệ nhị phân là: 0")
else:
    binary_number = ""  # Chuỗi để lưu kết quả nhị phân

    # Thực hiện chuyển đổi bằng cách chia liên tục cho 2
    while decimal_number > 0:
        remainder = decimal_number % 2  # Lấy phần dư
        binary_number = str(remainder) + binary_number  # Ghép phần dư vào trước kết quả
        decimal_number = decimal_number // 2  # Chia lấy phần nguyên

    # In kết quả
    print("Số ở hệ nhị phân là:", binary_number)
