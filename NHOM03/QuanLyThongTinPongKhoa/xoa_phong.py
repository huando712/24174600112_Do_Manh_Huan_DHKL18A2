from .file_utils import doc_danh_sach_phong, ghi_danh_sach_phong

def xoa_phong(ma_phong):
    danh_sach = doc_danh_sach_phong()
    danh_sach_moi = [phong for phong in danh_sach if phong["MaPhong"] != ma_phong]
    ghi_danh_sach_phong(danh_sach_moi)
    print(f"Xóa phòng có mã {ma_phong} thành công!")

