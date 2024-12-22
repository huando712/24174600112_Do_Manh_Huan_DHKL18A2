import csv
from QuanLyKhoa.view_khoa import ensure_file_exists, FILE_PATH

def delete_khoa():
    """Xóa một khoa."""
    ensure_file_exists()
    ma_khoa = input("Nhập mã khoa cần xóa: ")
    with open(FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    new_data = [row for row in data if row[0] != ma_khoa]
    if len(new_data) == len(data):
        print(f"Mã khoa '{ma_khoa}' không tồn tại!")
    else:
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print(f"Khoa '{ma_khoa}' đã được xóa.")
