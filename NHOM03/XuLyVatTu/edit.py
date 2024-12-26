# edit.py
import csv
import datetime

def edit_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        id_to_edit = input("Nhập mã vật tư cần chỉnh sửa: ")
        found = False
        for row in data:
            if row['Mã vật tư'] == id_to_edit:
                found = True
                print("Thông tin hiện tại:", row)
                for key in row:
                    if key not in ['Mã vật tư', 'Tháng', 'Năm']:
                        new_value = input(f"Nhập giá trị mới cho {key} (bỏ trống để giữ nguyên): ")
                        if new_value:
                            row[key] = new_value
                # Cập nhật thời gian chỉnh sửa
                row['Tháng'] = datetime.datetime.now().month
                row['Năm'] = datetime.datetime.now().year
                break

        if found:
            with open(file_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=row.keys())
                writer.writeheader()
                writer.writerows(data)
            print("Cập nhật thành công.")
        else:
            print("Không tìm thấy mã vật tư cần chỉnh sửa.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}.")