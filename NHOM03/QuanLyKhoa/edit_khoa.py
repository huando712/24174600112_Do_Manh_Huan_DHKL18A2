
import csv

FILE_PATH = "csv_file\ds_khoa.csv"  # Đường dẫn tệp CSV

def edit_khoa():
    """Sửa thông tin khoa."""
    # Kiểm tra nếu tệp không tồn tại
    try:
        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"Tệp '{FILE_PATH}' không tồn tại. Vui lòng tạo tệp trước khi chỉnh sửa.")
        return

    ma_khoa = input("Nhập mã khoa cần sửa: ")

    found = False
    for row in data:
        if row[0] == ma_khoa:
            print(f"Đang sửa khoa: {row}")
            row[1] = input("Nhập tên khoa mới: ") or row[1]
            row[2] = input("Nhập tổng số phòng mới: ") or row[2]
            found = True
            break

    if not found:
        print(f"Mã khoa '{ma_khoa}' không tồn tại!")
    else:
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Khoa '{ma_khoa}' đã được cập nhật.")
