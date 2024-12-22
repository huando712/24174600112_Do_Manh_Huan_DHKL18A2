import csv
from QuanLyKhoa.view_khoa import ensure_file_exists, FILE_PATH

def search_khoa():
    """Tìm kiếm một khoa."""
    ensure_file_exists()
    keyword = input("Nhập từ khóa tìm kiếm (mã hoặc tên khoa): ").lower()
    with open(FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        found = [row for row in data if keyword in row[0].lower() or keyword in row[1].lower()]

    if found:
        print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
        print("-" * 45)
        for row in found:
            print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))
    else:
        print("Không tìm thấy khoa nào phù hợp!")
