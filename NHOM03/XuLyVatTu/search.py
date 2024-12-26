# search.py
import csv
def search_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            query = input("Nhập thông tin cần tìm: ")
            print("Kết quả tìm kiếm:")
            for row in reader:
                if query in row.values():
                    print(row)
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}.")