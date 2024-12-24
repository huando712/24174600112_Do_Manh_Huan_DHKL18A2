

from QuanLyKhoa.view_khoa import view_khoa
from QuanLyKhoa.add_khoa import add_khoa
from QuanLyKhoa.edit_khoa import edit_khoa
from QuanLyKhoa.delete_khoa import delete_khoa
from QuanLyKhoa.search_khoa import search_khoa

from QuanLyThongTinPongKhoa import  xem_phong, them_phong, sua_phong, xoa_phong, tim_kiem_phong


from XuLyVatTu import  xem_phong_kem_vat_tu,  sua_vat_tu, xoa_vat_tu, tim_kiem_vat_tu

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

from XuLyVatTu.file_csv import doc_file_csv, luu_file_csv


def menu_vat_tu():
    """Hiển thị menu quản lý vật tư."""
    ds_vat_tu = []  # Khởi tạo danh sách rỗng
    file_path = "ds_vat_tu.csv"
    
    while True:
        print("\nQuản lý vật tư")
        print("1. Xem danh sách vật tư")
        print("2. Chỉnh sửa thông tin vật tư")
        print("3. Xóa thông tin vật tư")
        print("4. Tìm kiếm thông tin vật tư")
        print("5. Đọc danh sách từ file")
        print("6. Lưu danh sách vào file")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn: ").strip()
        
        if choice == "1":
            if not ds_vat_tu:
                print("Danh sách vật tư trống. Vui lòng thêm hoặc đọc từ file.")
            else:
                for item in ds_vat_tu:
                    print(item)
        
        elif choice == "2":
            if not ds_vat_tu:
                print("Danh sách vật tư trống. Vui lòng thêm hoặc đọc từ file.")
            else:
                ma_vat_tu = input("Nhập mã vật tư cần chỉnh sửa: ").strip()
                key = input("Nhập thuộc tính cần chỉnh sửa: ").strip()
                value = input("Nhập giá trị mới: ").strip()
                for vat_tu in ds_vat_tu:
                    if vat_tu["Ma vat tu"] == ma_vat_tu:
                        if key in vat_tu:
                            vat_tu[key] = value
                            print(f"Đã cập nhật thông tin cho vật tư {ma_vat_tu}.")
                        else:
                            print(f"Thuộc tính '{key}' không tồn tại.")
                        break
                else:
                    print(f"Không tìm thấy vật tư với mã {ma_vat_tu}.")
        
        elif choice == "3":
            if not ds_vat_tu:
                print("Danh sách vật tư trống. Vui lòng thêm hoặc đọc từ file.")
            else:
                ma_vat_tu = input("Nhập mã vật tư cần xóa: ").strip()
                ds_vat_tu = [vat_tu for vat_tu in ds_vat_tu if vat_tu["Ma vat tu"] != ma_vat_tu]
                print(f"Đã xóa vật tư với mã {ma_vat_tu}.")
        
        elif choice == "4":
            if not ds_vat_tu:
                print("Danh sách vật tư trống. Vui lòng thêm hoặc đọc từ file.")
            else:
                keyword = input("Nhập từ khóa tìm kiếm: ").strip()
                ket_qua = [vat_tu for vat_tu in ds_vat_tu if keyword in str(vat_tu.values())]
                if ket_qua:
                    for vat_tu in ket_qua:
                        print(vat_tu)
                else:
                    print("Không tìm thấy vật tư phù hợp.")
        
        elif choice == "5":
            ds_vat_tu = doc_file_csv(file_path)
            if ds_vat_tu:
                print("Đã đọc danh sách vật tư từ file.")
            else:
                print("Không có dữ liệu trong file hoặc file không tồn tại.")
        
        elif choice == "6":
            luu_file_csv(file_path, ds_vat_tu)
        
        elif choice == "0":
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")




        



def main_menu():
    """Hiển thị menu chính."""
    while True:
        print("\n--- Hệ Thống Quản Lý ---")
        print("1. Quản lý khoa")
        print("2. Quản lý thông tin phòng khoa")
        print("3. Quản lý vật tư")
        print("0. Thoát")
        try:
            choice = int(input("Chọn chức năng: "))
            if choice == 1:
                menu_khoa()
            elif choice == 2:
                menu_phong_khoa()
            elif choice == 3:
                menu_vat_tu()
            elif choice == 0:
                print("Thoát hệ thống quản lý.")
                break
            else:
                print("Vui lòng chọn số hợp lệ.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

if __name__ == "__main__":
    main_menu()