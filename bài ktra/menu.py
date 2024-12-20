# Danh sách cầu thủ
danh_sach_cau_thu = []

# Hàm nhập thông tin cầu thủ
def nhap_cau_thu():
    try:
        ma_cau_thu = input("Nhập mã cầu thủ: ")
        ten_cau_thu = input("Nhập tên cầu thủ: ")
        tuoi = int(input("Nhập tuổi cầu thủ (số nguyên): "))
        vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
        so_huy_chuong = int(input("Nhập số huy chương (số nguyên): "))
        
        if tuoi <= 0 or so_huy_chuong < 0:
            raise ValueError("Tuổi hoặc số huy chương không thể âm hoặc bằng 0.")
        
        danh_sach_cau_thu.append({
            "ma": ma_cau_thu,
            "ten": ten_cau_thu,
            "tuoi": tuoi,
            "vi_tri": vi_tri,
            "so_huy_chuong": so_huy_chuong,
            "thuong": 0  # Sẽ tính sau
        })
        print("Đã thêm cầu thủ thành công!")
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Hàm tính cột thưởng
def tinh_thuong():
    try:
        for cau_thu in danh_sach_cau_thu:
            so_huy_chuong = cau_thu["so_huy_chuong"]
            if so_huy_chuong > 10:
                cau_thu["thuong"] = so_huy_chuong * 500000
            elif 5 <= so_huy_chuong <= 10:
                cau_thu["thuong"] = so_huy_chuong * 300000
            else:
                cau_thu["thuong"] = so_huy_chuong * 200000
        print("Đã tính thưởng cho tất cả cầu thủ.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi tính thưởng: {e}")

# Hàm hiển thị danh sách cầu thủ
def xem_danh_sach():
    try:
        if not danh_sach_cau_thu:
            print("Danh sách cầu thủ đang trống.")
            return
        print("\nDanh sách cầu thủ:")
        for cau_thu in danh_sach_cau_thu:
            print(f"Mã: {cau_thu['ma']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
                  f"Vị trí: {cau_thu['vi_tri']}, Số huy chương: {cau_thu['so_huy_chuong']}, "
                  f"Thưởng: {cau_thu['thuong']}")
    except Exception as e:
        print(f"Có lỗi xảy ra khi hiển thị danh sách: {e}")

# Hàm tìm kiếm và xóa cầu thủ theo mã
def tim_kiem_xoa_cau_thu():
    try:
        ma_can_xoa = input("Nhập mã cầu thủ cần xóa: ")
        for cau_thu in danh_sach_cau_thu:
            if cau_thu["ma"] == ma_can_xoa:
                danh_sach_cau_thu.remove(cau_thu)
                print(f"Đã xóa cầu thủ có mã {ma_can_xoa}.")
                return
        print(f"Không tìm thấy cầu thủ có mã {ma_can_xoa}.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi xóa cầu thủ: {e}")

# Hàm tìm kiếm và chỉnh sửa thông tin cầu thủ theo mã
def tim_kiem_chinh_sua_cau_thu():
    try:
        ma_can_sua = input("Nhập mã cầu thủ cần chỉnh sửa: ")
        for cau_thu in danh_sach_cau_thu:
            if cau_thu["ma"] == ma_can_sua:
                print("Cầu thủ hiện tại:")
                print(f"Mã: {cau_thu['ma']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
                      f"Vị trí: {cau_thu['vi_tri']}, Số huy chương: {cau_thu['so_huy_chuong']}, "
                      f"Thưởng: {cau_thu['thuong']}")
                
                cau_thu["ten"] = input("Nhập tên mới: ") or cau_thu["ten"]
                cau_thu["tuoi"] = int(input("Nhập tuổi mới (để trống nếu không đổi): ") or cau_thu["tuoi"])
                cau_thu["vi_tri"] = input("Nhập vị trí mới (để trống nếu không đổi): ") or cau_thu["vi_tri"]
                cau_thu["so_huy_chuong"] = int(input("Nhập số huy chương mới (để trống nếu không đổi): ") or cau_thu["so_huy_chuong"])
                
                print(f"Đã chỉnh sửa thông tin cầu thủ có mã {ma_can_sua}.")
                return
        print(f"Không tìm thấy cầu thủ có mã {ma_can_sua}.")
    except ValueError:
        print("Dữ liệu nhập không hợp lệ.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi chỉnh sửa cầu thủ: {e}")
# Hàm hiển thị danh sách cầu thủ và sắp xếp theo huy chương
def xem_danh_sach():
    try:
        if not danh_sach_cau_thu:
            print("Danh sách cầu thủ đang trống.")
            return
        
        # Sắp xếp danh sách cầu thủ theo số huy chương từ nhỏ đến lớn
        danh_sach_sap_xep = sorted(danh_sach_cau_thu, key=lambda x: x['so_huy_chuong'])
        
        print("\nDanh sách cầu thủ (Sắp xếp theo huy chương từ nhỏ đến lớn):")
        for cau_thu in danh_sach_sap_xep:
            print(f"Mã: {cau_thu['ma']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
                  f"Vị trí: {cau_thu['vi_tri']}, Số huy chương: {cau_thu['so_huy_chuong']}, "
                  f"Thưởng: {cau_thu['thuong']}")
    except Exception as e:
        print(f"Có lỗi xảy ra khi hiển thị danh sách: {e}")
# Menu chương trình
# Menu chương trình
def menu():
    while True:
        print("\nChương trình quản lý đội bóng:")
        print("1. Xem danh sách cầu thủ")
        
        print("2. Nhập thông tin cầu thủ")
        print("3. Tính cột thưởng")
        print("4. Tìm kiếm và xóa cầu thủ")

        print("5. Tìm kiếm và chỉnh sửa cầu thủ")
        print("6. Xem danh sách cầu thủ sắp xếp theo huy chương")
        print("7. Thoát")
        
        try:
            lua_chon = int(input("Nhập lựa chọn của bạn (1-7): "))
            if lua_chon == 1:
                xem_danh_sach()
            elif lua_chon == 2:
                xem_danh_sach()  # Tùy chọn này sẽ gọi hàm đã sửa trên
            elif lua_chon == 3:
                nhap_cau_thu()
            elif lua_chon == 4:
                tinh_thuong()
            elif lua_chon == 5:
                tim_kiem_xoa_cau_thu()
            elif lua_chon == 6:
                tim_kiem_chinh_sua_cau_thu()
            elif lua_chon == 7:
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 7.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
menu()