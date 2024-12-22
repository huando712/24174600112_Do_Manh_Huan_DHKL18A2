import csv

FILE_PATH = 'csv_file/ds_khoa.csv'

def ensure_file_exists():
    """Đảm bảo tệp CSV tồn tại."""
    try:
        with open(FILE_PATH, mode='r') as file:
            pass
    except FileNotFoundError:
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Mã Khoa", "Tên Khoa", "Tổng Số Phòng"])

def view_khoa():
    """Hiển thị danh sách khoa."""
    ensure_file_exists()
    with open(FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) <= 1:
            print("Danh sách khoa trống!")
            return
        print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
        print("-" * 45)
        for row in data[1:]:
            print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))

