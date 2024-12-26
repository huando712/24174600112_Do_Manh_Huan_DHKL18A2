
# delete.py
import csv
import datetime

def delete_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        id_to_delete = input("Nhập mã vật tư cần xóa: ")
        new_data = [row for row in data if row['Mã vật tư'] != id_to_delete]

        if len(new_data) != len(data):
            with open(file_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(new_data)
            print("Xóa thành công.")

            # Ghi nhật ký xóa với datetime
            with open("delete_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"Xóa mã vật tư: {id_to_delete} vào {datetime.datetime.now()}\n")
        else:
            print("Không tìm thấy mã vật tư cần xóa.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}.")