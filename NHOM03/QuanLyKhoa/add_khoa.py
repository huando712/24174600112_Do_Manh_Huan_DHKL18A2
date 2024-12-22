import csv
from QuanLyKhoa.view_khoa import ensure_file_exists, FILE_PATH

def add_khoa():
    """Thêm một khoa mới."""
    ensure_file_exists()
    ma_khoa = input("Nhập mã khoa: ")
    ten_khoa = input("Nhập tên khoa: ")
    tong_phong = input("Nhập tổng số phòng: ")
    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ma_khoa, ten_khoa, tong_phong])
    print(f"Khoa '{ten_khoa}' đã được thêm.")
