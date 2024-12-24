
import csv
from datetime import datetime

def doc_file_csv(file_path):
    """Đọc danh sách vật tư từ file CSV."""
    ds_vat_tu = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row["Thang"] = datetime.strptime(row["Thang"], "%Y-%m-%d")
                    row["Nam"] = datetime.strptime(row["Nam"], "%Y-%m-%d")
                except ValueError as e:
                    print(f"Lỗi định dạng ngày trong dòng {row}: {e}")
                    continue
                ds_vat_tu.append(row)
    except FileNotFoundError:
        print(f"File {file_path} không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file: {e}")
    return ds_vat_tu

def luu_file_csv(file_path, ds_vat_tu):
    """Lưu danh sách vật tư vào file CSV."""
    if not ds_vat_tu:
        print("Danh sách vật tư trống, không có dữ liệu để lưu.")
        return

    try:
        with open(file_path, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["Ma phong", "Tong so bo ban ghe", "Tong so man hinh", "Tong so dieu hoa", 
                          "So bo ban ghe hong", "So man hinh hong", "So dieu hoa hong", "Thang", "Nam", "Ma vat tu"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for vat_tu in ds_vat_tu:
                vat_tu["Thang"] = vat_tu["Thang"].strftime("%Y-%m-%d")
                vat_tu["Nam"] = vat_tu["Nam"].strftime("%Y-%m-%d")
                writer.writerow(vat_tu)
        print(f"Đã lưu danh sách vật tư vào {file_path}.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi lưu file: {e}")
