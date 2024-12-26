
import csv

FILE_PATH = 'csv_file\ds_khoa.csv'  # đường dẫn tệp 

def add_khoa():
    """Thêm một khoa mới."""
    try:
        # Cố gắng mở tệp để kiểm tra sự tồn tại
        with open(FILE_PATH, mode='r', newline='') as file:
            pass  # Nếu mở tệp thành công, không làm gì cả
    except FileNotFoundError:
        # Nếu tệp không tồn tại, tạo một tệp mới và thêm tiêu đề
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Mã khoa', 'Tên khoa', 'Tổng số phòng'])
    
    ma_khoa = input("Nhập mã khoa: ")  # Nhập các yêu cầu vô
    ten_khoa = input("Nhập tên khoa: ")
    tong_phong = input("Nhập tổng số phòng: ")

    with open(FILE_PATH, mode='a', newline='') as file:  # Mở tệp ở chế độ append
        writer = csv.writer(file)
        writer.writerow([ma_khoa, ten_khoa, tong_phong])  # Ghi dữ liệu vào tệp

    print(f"Khoa '{ten_khoa}' đã được thêm.")  # In lên màn hình

