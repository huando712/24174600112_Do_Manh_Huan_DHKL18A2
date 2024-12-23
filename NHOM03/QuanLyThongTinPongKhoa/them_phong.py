from .file_utils import doc_danh_sach_phong, ghi_danh_sach_phong

def them_phong(phong_moi):
    danh_sach = doc_danh_sach_phong()
    danh_sach.append(phong_moi)
    ghi_danh_sach_phong(danh_sach)
    print("Thêm phòng thành công!")
