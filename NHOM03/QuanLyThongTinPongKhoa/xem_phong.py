from .file_utils import doc_danh_sach_phong

def xem_danh_sach_phong():
    danh_sach = doc_danh_sach_phong()
    if not danh_sach:
        print("Danh sách phòng trống.")
    else:
        for phong in danh_sach:
            print(phong)

