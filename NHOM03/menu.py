#menu
from QuanLyKhoa.view_khoa import view_khoa
from QuanLyKhoa.add_khoa import add_khoa
from QuanLyKhoa.edit_khoa import edit_khoa
from QuanLyKhoa.delete_khoa import delete_khoa
from QuanLyKhoa.search_khoa import search_khoa

from QuanLyThongTinPongKhoa import  xem_phong, them_phong, sua_phong, xoa_phong, tim_kiem_phong


from XuLyVatTu import  delete, doc_luu_file, edit, search, view

def menu_khoa():
    """Hiển thị menu quản lý khoa."""
    while True:
        print("\n--- Quản Lý Khoa ---")
        print("1. Xem danh sách khoa")
        print("2. Thêm khoa")
        print("3. Sửa khoa")
        print("4. Xóa khoa")
        print("5. Tìm kiếm khoa")
        print("0. Quay lại menu chính")
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
                break
            else:
                print("Vui lòng chọn số hợp lệ.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

def menu_phong_khoa():
    """Hiển thị menu quản lý Thông Tin phòng khoa."""
    while True:
        print("\n--- Quản Lý Thông Tin Phòng Khoa ---")
        print("1. Xem danh sách phòng")
        print("2. Thêm phòng")
        print("3. Sửa phòng")
        print("4. Xóa phòng")
        print("5. Tìm kiếm phòng")
        print("0. Quay lại menu chính")
        try:
            choice = int(input("Chọn chức năng: "))
            if choice == 1:
                xem_phong.xem_danh_sach_phong()
            elif choice == 2:
                ma_phong = input("Nhập mã phòng: ").strip()
                ten_phong = input("Nhập tên phòng: ").strip()
                loai_phong = int(input("Nhập loại phòng (0, 1, 2): ").strip())
                vi_tri_khu_nha = int(input("Nhập vị trí khu nhà (0-5): ").strip())
                vi_tri_tang = int(input("Nhập vị trí tầng: ").strip())
                sdt_quan_ly = input("Nhập số điện thoại quản lý: ").strip()
                ma_khoa = input("Nhập mã khoa: ").strip()

                phong_moi = {
                    "MaPhong": ma_phong,
                    "TenPhong": ten_phong,
                    "LoaiPhong": loai_phong,
                    "ViTriKhuNha": vi_tri_khu_nha,
                    "ViTriTang": vi_tri_tang,
                    "SDTQuanLy": sdt_quan_ly,
                    "MaKhoa": ma_khoa,
                }
                them_phong.them_phong(phong_moi)
            elif choice == 3:
                ma_phong = input("Nhập mã phòng cần sửa: ").strip()
                print("Nhập các thông tin mới (để trống nếu không muốn thay đổi):")
                ten_phong = input("Tên phòng: ").strip()
                loai_phong = input("Loại phòng (0, 1, 2): ").strip()
                vi_tri_khu_nha = input("Vị trí khu nhà (0-5): ").strip()
                vi_tri_tang = input("Vị trí tầng: ").strip()
                sdt_quan_ly = input("Số điện thoại quản lý: ").strip()
                ma_khoa = input("Mã khoa: ").strip()

                thong_tin_moi = {}
                if ten_phong:
                    thong_tin_moi["TenPhong"] = ten_phong
                if loai_phong:
                    thong_tin_moi["LoaiPhong"] = int(loai_phong)
                if vi_tri_khu_nha:
                    thong_tin_moi["ViTriKhuNha"] = int(vi_tri_khu_nha)
                if vi_tri_tang:
                    thong_tin_moi["ViTriTang"] = int(vi_tri_tang)
                if sdt_quan_ly:
                    thong_tin_moi["SDTQuanLy"] = sdt_quan_ly
                if ma_khoa:
                    thong_tin_moi["MaKhoa"] = ma_khoa

                sua_phong.sua_phong(ma_phong, thong_tin_moi)
            elif choice == 4:
                ma_phong = input("Nhập mã phòng cần xóa: ").strip()
                xoa_phong.xoa_phong(ma_phong)
            elif choice == 5:
                ma_phong = input("Nhập mã phòng cần tìm: ").strip()
                tim_kiem_phong.tim_kiem_phong(ma_phong)
            elif choice == 0:
                break
            else:
                print("Vui lòng chọn số hợp lệ.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

from XuLyVatTu import delete, edit, search, view

# Đường dẫn file dữ liệu
FILE_PATH = 'csv_file\ds_vat_tu.csv'

def menu_vat_tu():
    while True:
        print("\n--- Xử lý Vật Tư ---")
        print("1. Xem phòng kèm vật tư")
        print("2. Chỉnh sửa thông tin vật tư")
        print("3. Xóa thông tin vật tư")
        print("4. Tìm kiếm thông tin vật tư")
        print("5. Đọc và lưu danh sách vào file")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            view.view_data(FILE_PATH)
        elif choice == '2':
            edit.edit_data(FILE_PATH)
        elif choice == '3':
            delete.delete_data(FILE_PATH)
        elif choice == '4':
            search.search_data(FILE_PATH)
        elif choice == '5':
            doc_luu_file.read_and_save(FILE_PATH)
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
from ChucNangKhac  import kiem_tra_khoa
from ChucNangKhac import kiem_tra_phong_khoa
from ChucNangKhac import kiem_tra_vat_tu
from ChucNangKhac import sap_xep

def menu_khac():
    print("=== Chức năng khác ===")
    print("1. Kiểm tra input cho khoa")
    print("2. Kiểm tra input cho phòng khoa")
    print("3. Kiểm tra input cho vật tư")
    print("4. Sắp xếp danh sách")
    choice = input("Chọn chức năng: ")
    if choice == "1":
        kiem_tra_khoa.check_input()
    elif choice == "2":
        kiem_tra_phong_khoa.check_input()
    elif choice == "3":
        kiem_tra_vat_tu.check_input()
    elif choice == "4":
        menu_sap_xep()

def menu_sap_xep():
    print("=== Sắp xếp danh sách ===")
    print("1. Sắp xếp danh sách khoa")
    print("2. Sắp xếp danh sách phòng khoa")
    print("3. Sắp xếp danh sách vật tư")
    print("0. Quay lại")
    
    choice = input("Chọn danh sách muốn sắp xếp: ")
    
    if choice == "1":
        sap_xep.sort_khoa()  # Thực hiện sắp xếp khoa
    elif choice == "2":
        sap_xep.sort_phong_khoa()  # Thực hiện sắp xếp phòng khoa
    elif choice == "3":
        sap_xep.sort_vat_tu()  # Thực hiện sắp xếp vật tư
    elif choice == "0":
        print("Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def main_menu():
    """Hiển thị menu chính."""
    while True:
        print("\n--- Hệ Thống Quản Lý ---")
        print("1. Quản lý khoa")
        print("2. Quản lý thông tin phòng khoa")
        print("3. Xử lý vật tư")
        print("4. Các chức năng khác")
        print("0. Thoát")
        try:
            choice = int(input("Chọn chức năng: "))
            if choice == 1:
                menu_khoa()
            elif choice == 2:
                menu_phong_khoa()
            elif choice == 3:
                menu_vat_tu()
            elif choice == 4:
                menu_khac()
            elif choice == 0:
                print("Thoát hệ thống quản lý.")
                break
            else:
                print("Vui lòng chọn số hợp lệ.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

if __name__ == "__main__":
    main_menu()