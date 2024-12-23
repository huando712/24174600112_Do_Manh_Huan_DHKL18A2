import csv #mở thư viện
from QuanLyKhoa.view_khoa import ensure_file_exists, FILE_PATH # form để có thể chạy ở file menu.py

def add_khoa():
    """Thêm một khoa mới."""
    ensure_file_exists() #kiểm tra xem tệp có tồn tại hay không
    ma_khoa = input("Nhập mã khoa: ")#nhập các yêu cầu vô
    ten_khoa = input("Nhập tên khoa: ")
    tong_phong = input("Nhập tổng số phòng: ")
    with open(FILE_PATH, mode='a', newline='') as file:#newline là xóa cách khoảng trống
        #mode='a': Chế độ mở tệp là "append", tức là nếu tệp đã tồn tại, dữ liệu sẽ được thêm vào cuối tệp thay vì ghi đè lên dữ liệu cũ.
        writer = csv.writer(file)
        #, writer giúp bạn ghi dữ liệu vào tệp CSV theo định dạng bảng, với mỗi giá trị trong một danh sách sẽ là một ô trong bảng.

        writer.writerow([ma_khoa, ten_khoa, tong_phong])#ghi các yêu cầu của bài
    print(f"Khoa '{ten_khoa}' đã được thêm.")#in lên màn

