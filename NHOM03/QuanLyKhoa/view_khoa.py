import csv
import os

FILE_PATH = 'csv_file/ds_khoa.csv'

def ensure_file_exists():
    """Đảm bảo thư mục và tệp CSV tồn tại."""
    dir_path = os.path.dirname(FILE_PATH)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Mã Khoa", "Tên Khoa", "Tổng Số Phòng"])  # Tạo tiêu đề cột

def view_khoa():
    """Hiển thị danh sách khoa."""
    ensure_file_exists()
    with open(FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) <= 1:  # Không có dữ liệu
            print("Danh sách khoa trống!")
            return
        print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
        print("-" * 45)
        for row in data[1:]:
            print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))
