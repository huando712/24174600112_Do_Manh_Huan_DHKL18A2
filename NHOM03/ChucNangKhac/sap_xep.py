import csv

def sap_xep_danh_sach(file_csv, cot_sap_xep, tang_dan=True):
    """
    Hàm sắp xếp dữ liệu từ file CSV theo một cột cụ thể.
    
    Args:
        file_csv (str): Đường dẫn đến file CSV cần sắp xếp.
        cot_sap_xep (str): Tên cột cần sắp xếp.
        tang_dan (bool): True để sắp xếp tăng dần, False để sắp xếp giảm dần.
    """
    try:
        with open(file_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        if not data:
            print("File CSV không có dữ liệu.")
            return

        # Kiểm tra cột sắp xếp có tồn tại không
        if cot_sap_xep not in data[0]:
            print(f"Cột '{cot_sap_xep}' không tồn tại trong file CSV.")
            return
        
        # Sắp xếp dữ liệu
        data_sorted = sorted(data, key=lambda x: x[cot_sap_xep], reverse=not tang_dan)
        
        # Ghi lại dữ liệu đã sắp xếp vào file
        with open(file_csv, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data_sorted)
        
        print(f"Danh sách đã được sắp xếp theo cột '{cot_sap_xep}' {'tăng' if tang_dan else 'giảm'} dần.")
    
    except FileNotFoundError:
        print(f"File '{file_csv}' không tồn tại.")
    except Exception as e:
        print(f"Lỗi khi sắp xếp: {e}")


def sort_khoa():
    print("=== Sắp xếp danh sách khoa ===")
    cot = input("Nhập tên cột muốn sắp xếp (ví dụ: Tên, Mã): ")
    tang_dan = input("Sắp xếp tăng dần? (y/n): ").lower() == 'y'
    sap_xep_danh_sach("csv_file/ds_khoa.csv", cot, tang_dan)

def sort_phong_khoa():
    print("=== Sắp xếp danh sách phòng khoa ===")
    cot = input("Nhập tên cột muốn sắp xếp (ví dụ: Tên phòng, Mã phòng): ")
    tang_dan = input("Sắp xếp tăng dần? (y/n): ").lower() == 'y'
    sap_xep_danh_sach("csv_file/ds_phong_khoa.csv", cot, tang_dan)


def sort_vat_tu():
    print("=== Sắp xếp danh sách vật tư ===")
    cot = input("Nhập tên cột muốn sắp xếp (ví dụ: Tên vật tư, Số lượng): ")
    tang_dan = input("Sắp xếp tăng dần? (y/n): ").lower() == 'y'
    sap_xep_danh_sach("csv_file/ds_vat_tu.csv", cot, tang_dan)
