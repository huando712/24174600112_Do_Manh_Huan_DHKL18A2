
import csv

FILE_PATH = 'csv_file/ds_khoa.csv'

def ensure_file_exists(file_path=FILE_PATH, headers=None):
    """Đảm bảo tệp CSV tồn tại, nếu không sẽ tạo với các cột mặc định."""
    if headers is None:
        headers = ["Mã Khoa", "Tên Khoa", "Tổng Số Phòng"]
    try:
        with open(file_path, mode='r') as file:
            pass
    except FileNotFoundError:
        # Tạo tệp mới với tiêu đề cột nếu tệp không tồn tại
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

def validate_string_length(value, max_length):
    """Đảm bảo chuỗi không vượt quá độ dài tối đa."""
    return value[:max_length] if len(value) > max_length else value

def view_khoa():
    """Hiển thị danh sách khoa từ tệp CSV."""
    ensure_file_exists(FILE_PATH, ["Mã Khoa", "Tên Khoa", "Tổng Số Phòng"])
    
    try:
        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            
            if len(data) <= 1:  # Kiểm tra nếu không có dữ liệu
                print("Danh sách khoa trống!")
                return
            
            # Hiển thị tiêu đề
            print("{:<10} {:<20} {:<15}".format("Mã Khoa", "Tên Khoa", "Tổng Số Phòng"))
            print("-" * 45)
            
            for row in data[1:]:  # Bỏ qua dòng tiêu đề
                try:
                    row[2] = int(row[2]) if row[2] else 0  # Đảm bảo Tổng Số Phòng là số nguyên
                except ValueError:
                    row[2] = 0
                print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))

    except Exception as e:
        print(f"Lỗi khi đọc tệp: {e}")






# Đây là một hàm mà bạn gọi trước khi mở tệp để đảm bảo rằng tệp CSV (chứa dữ liệu khoa) tồn tại. Nếu tệp không tồn tại, bạn có thể thêm mã để tạo tệp hoặc thông báo lỗi.
# with open(FILE_PATH, mode='r') as file::

# Mở tệp CSV (được chỉ định bởi FILE_PATH) ở chế độ đọc ('r'). Việc sử dụng with open đảm bảo rằng tệp sẽ được đóng tự động sau khi xong.
# reader = csv.reader(file):

# Sử dụng thư viện csv để đọc nội dung của tệp CSV. csv.reader sẽ đọc dữ liệu từ tệp và trả về các dòng dữ liệu dưới dạng danh sách.
# data = list(reader):

# Chuyển đối tượng reader thành một danh sách (list) để có thể dễ dàng thao tác với dữ liệu. Mỗi phần tử của data là một danh sách con, tương ứng với một dòng trong tệp CSV.
# if len(data) <= 1::

# Kiểm tra nếu tệp không chứa dữ liệu hoặc chỉ có dòng tiêu đề (dòng đầu tiên), thì hàm sẽ in ra thông báo "Danh sách khoa trống!" và dừng thực hiện hàm.
# In ra dòng tiêu đề cho bảng, với định dạng cột:
# Cột "Mã Khoa" có chiều rộng là 10 ký tự.
# Cột "Tên Khoa" có chiều rộng là 20 ký tự.
# Cột "Tổng Số Phòng" có chiều rộng là 15 ký tự.
# print("-" * 45):

# In ra một dòng phân cách để tách tiêu đề và dữ liệu, giúp bảng trở nên dễ đọc hơn.
# for row in data[1:]::

# Vòng lặp này duyệt qua tất cả các dòng dữ liệu trong tệp CSV, bắt đầu từ dòng thứ hai (dòng đầu tiên thường là tiêu đề, nên được bỏ qua). data[1:] chỉ lấy các dòng từ chỉ mục 1 trở đi.
# print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2])):

# In ra thông tin về mỗi khoa. Mỗi dòng của tệp CSV được chứa trong biến row, và các phần tử của row được in theo định dạng đã chỉ định:
# row[0]: Mã khoa (dự kiến ở cột đầu tiên trong tệp CSV).
# row[1]: Tên khoa (dự kiến ở cột thứ hai).
# row[2]: Tổng số phòng (dự kiến ở cột thứ ba).