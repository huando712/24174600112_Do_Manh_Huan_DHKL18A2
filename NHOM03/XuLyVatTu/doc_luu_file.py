# file_handler.py
import csv
import datetime

def read_and_save(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            print("Dữ liệu hiện tại trong file:")
            for row in data:
                print(row)

        # Lưu dữ liệu vào một file CSV mới
        new_file_path = f"dsvattu_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(new_file_path, 'w', encoding='utf-8', newline='') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Dữ liệu đã được  lưu vào file: {new_file_path}")
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}.")