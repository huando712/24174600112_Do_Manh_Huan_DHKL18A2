
import csv

FILE_PATH = 'csv_file\ds_khoa.csv'  

def delete_khoa():
    """Xóa một khoa."""
    try:
        # Cố gắng mở tệp để kiểm tra sự tồn tại
        with open(FILE_PATH, mode='r') as file:
            data = list(csv.reader(file))  # Đọc dữ liệu từ tệp
    except FileNotFoundError:
        print(f"Tệp '{FILE_PATH}' không tồn tại!")
        return  # Dừng hàm nếu tệp không tồn tại

    ma_khoa = input("Nhập mã khoa cần xóa: ")

    # Lọc các dòng không có mã khoa cần xóa
    new_data = [row for row in data if row[0] != ma_khoa]

    # Kiểm tra xem có khoa nào bị xóa không
    if len(new_data) == len(data):
        print(f"Mã khoa '{ma_khoa}' không tồn tại!")
    else:
        # Ghi lại dữ liệu mới vào tệp
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print(f"Khoa '{ma_khoa}' đã được xóa.")
