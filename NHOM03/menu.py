# import csv
# import os

# FILE_PATH = 'csv_file/ds_khoa.csv'

# def ensure_file_exists():
#     """Đảm bảo thư mục và tệp CSV tồn tại."""
#     dir_path = os.path.dirname(FILE_PATH)
#     if not os.path.exists(dir_path):
#         print(f"Thư mục '{dir_path}' không tồn tại! Tạo thư mục mới...")
#         os.makedirs(dir_path)
#     if not os.path.exists(FILE_PATH):
#         print("Tệp ds_khoa.csv không tồn tại! Tạo tệp mới...")
#         with open(FILE_PATH, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["Mã Khoa", "Tên Khoa", "Tổng Số Phòng"])  # Tạo tiêu đề cột

# def view_khoa():
#     """Hiển thị danh sách khoa."""
#     ensure_file_exists()
#     with open(FILE_PATH, mode='r') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         if len(data) <= 1:  # Chỉ có tiêu đề, không có dữ liệu
#             print("Danh sách khoa trống!")
#             return
#         print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
#         print("-" * 45)
#         for row in data[1:]:
#             print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))

# def add_khoa():
#     """Thêm một khoa mới."""
#     ensure_file_exists()
#     ma_khoa = input("Nhập mã khoa: ")
#     ten_khoa = input("Nhập tên khoa: ")
#     tong_phong = input("Nhập tổng số phòng: ")
#     with open(FILE_PATH, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([ma_khoa, ten_khoa, tong_phong])
#     print(f"Khoa '{ten_khoa}' đã được thêm.")

# def edit_khoa():
#     """Sửa thông tin khoa."""
#     ensure_file_exists()
#     ma_khoa = input("Nhập mã khoa cần sửa: ")
#     with open(FILE_PATH, mode='r') as file:
#         reader = csv.reader(file)
#         data = list(reader)

#     found = False
#     for row in data:
#         if row[0] == ma_khoa:
#             print(f"Đang sửa khoa: {row}")
#             row[1] = input("Nhập tên khoa mới: ") or row[1]
#             row[2] = input("Nhập tổng số phòng mới: ") or row[2]
#             found = True
#             break

#     if not found:
#         print(f"Mã khoa '{ma_khoa}' không tồn tại!")
#     else:
#         with open(FILE_PATH, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(data)
#         print(f"Khoa '{ma_khoa}' đã được cập nhật.")

# def delete_khoa():
#     """Xóa một khoa."""
#     ensure_file_exists()
#     ma_khoa = input("Nhập mã khoa cần xóa: ")
#     with open(FILE_PATH, mode='r') as file:
#         reader = csv.reader(file)
#         data = list(reader)

#     new_data = [row for row in data if row[0] != ma_khoa]
#     if len(new_data) == len(data):
#         print(f"Mã khoa '{ma_khoa}' không tồn tại!")
#     else:
#         with open(FILE_PATH, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(new_data)
#         print(f"Khoa '{ma_khoa}' đã được xóa.")

# def search_khoa():
#     """Tìm kiếm một khoa."""
#     ensure_file_exists()
#     keyword = input("Nhập từ khóa tìm kiếm (mã hoặc tên khoa): ").lower()
#     with open(FILE_PATH, mode='r') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         found = [row for row in data if keyword in row[0].lower() or keyword in row[1].lower()]

#     if found:
#         print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
#         print("-" * 45)
#         for row in found:
#             print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))
#     else:
#         print("Không tìm thấy khoa nào phù hợp!")

# def menu():
#     """Hiển thị menu chính."""
#     while True:
#         print("\n--- Quản Lý Khoa ---")
#         print("1. Xem danh sách khoa")
#         print("2. Thêm khoa")
#         print("3. Sửa khoa")
#         print("4. Xóa khoa")
#         print("5. Tìm kiếm khoa")
#         print("0. Thoát")
#         try:
#             choice = int(input("Chọn chức năng: "))
#             if choice == 1:
#                 view_khoa()
#             elif choice == 2:
#                 add_khoa()
#             elif choice == 3:
#                 edit_khoa()
#             elif choice == 4:
#                 delete_khoa()
#             elif choice == 5:
#                 search_khoa()
#             elif choice == 0:
#                 print("Thoát chương trình.")
#                 break
#             else:
#                 print("Vui lòng chọn số hợp lệ.")
#         except ValueError:
#             print("Lỗi: Vui lòng nhập một số hợp lệ.")

# if __name__ == "__main__":
#     menu()
from QuanLyKhoa.view_khoa import view_khoa
from QuanLyKhoa.add_khoa import add_khoa
from QuanLyKhoa.edit_khoa import edit_khoa
from QuanLyKhoa.delete_khoa import delete_khoa
from QuanLyKhoa.search_khoa import search_khoa

def menu():
    """Hiển thị menu chính."""
    while True:
        print("\n--- Quản Lý Khoa ---")
        print("1. Xem danh sách khoa")
        print("2. Thêm khoa")
        print("3. Sửa khoa")
        print("4. Xóa khoa")
        print("5. Tìm kiếm khoa")
        print("0. Thoát")
        try:
            choice = int(input("Chọn chức năng: "))
            if choice == 1:
                view_khoa()
            elif choice == 2:
                add_khoa()
            elif choice == 3:
                edit_khoa()
            elif choice == 4:
                delete_khoa()
            elif choice == 5:
                search_khoa()
            elif choice == 0:
                print("Thoát chương trình.")
                break
            else:
                print("Vui lòng chọn số hợp lệ.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

if __name__ == "__main__":
    menu()
