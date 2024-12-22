import csv
from QuanLyKhoa.view_khoa import ensure_file_exists, FILE_PATH

def edit_khoa():
    """Sửa thông tin khoa."""
    ensure_file_exists()
    ma_khoa = input("Nhập mã khoa cần sửa: ")
    with open(FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

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
