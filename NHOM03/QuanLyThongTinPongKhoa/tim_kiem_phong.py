from .file_utils import doc_danh_sach_phong

def tim_kiem_phong(ma_phong):
    danh_sach = doc_danh_sach_phong()
    for phong in danh_sach:
        if phong["MaPhong"] == ma_phong:
            print("Thông tin phòng:", phong)
            return
    print(f"Không tìm thấy phòng có mã {ma_phong}.")
