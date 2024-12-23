import csv

FILE_PATH = "ds_phong_khoa.csv"

def doc_danh_sach_phong():
    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def ghi_danh_sach_phong(danh_sach):
    with open(FILE_PATH, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["MaPhong", "TenPhong", "LoaiPhong", "ViTriKhuNha", "ViTriTang", "SDTQuanLy", "MaKhoa"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(danh_sach)
