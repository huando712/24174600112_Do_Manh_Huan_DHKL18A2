file_path = "XuLyVatTu"
def kiem_tra_input_vat_tu(data):
    if not data.get("ma_vat_tu") or not data.get("ten_vat_tu"):
        return False, "Thiếu mã vật tư hoặc tên vật tư."
    return True, "Dữ liệu hợp lệ."
