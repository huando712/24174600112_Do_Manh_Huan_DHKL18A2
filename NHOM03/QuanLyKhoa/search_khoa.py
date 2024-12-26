
import csv

FILE_PATH = 'csv_file\ds_khoa.csv'

def search_khoa():
    """Tìm kiếm một khoa."""
    try:
        # Cố gắng mở tệp để kiểm tra sự tồn tại
        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"Tệp '{FILE_PATH}' không tồn tại!")
        return  # Dừng hàm nếu tệp không tồn tại

    keyword = input("Nhập từ khóa tìm kiếm (mã hoặc tên khoa): ").lower()

    # Tìm các dòng có chứa từ khóa
    found = [row for row in data if keyword in row[0].lower() or keyword in row[1].lower()]

    if found:
        print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
        print("-" * 45)
        for row in found:
            print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))
    else:
        print("Không tìm thấy khoa nào phù hợp!")
