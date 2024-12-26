def check_input():
    print("=== Kiểm tra input cho phòng khoa ===")
    input_data = input("Nhập dữ liệu cho phòng khoa: ")
    if input_data.strip():
        print(f"Dữ liệu hợp lệ: {input_data}")
    else:
        print("Dữ liệu không hợp lệ.")


