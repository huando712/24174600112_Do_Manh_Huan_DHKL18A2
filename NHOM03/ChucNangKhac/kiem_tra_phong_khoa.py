
def kiem_tra_input_phong_khoa(data):
    if not data.get("ma_phong") or not data.get("ten_phong"):
        return False, "Thiếu mã phòng hoặc tên phòng."
    return True, "Dữ liệu hợp lệ."
