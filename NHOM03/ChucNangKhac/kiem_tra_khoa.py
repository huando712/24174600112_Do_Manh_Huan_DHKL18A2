file_path = "QuanLyKhoa"
def kiem_tra_input_khoa(data):
    if not data.get("ma_khoa") or not data.get("ten_khoa"):
        return False, "Thiếu mã khoa hoặc tên khoa."
    return True, "Dữ liệu hợp lệ."
