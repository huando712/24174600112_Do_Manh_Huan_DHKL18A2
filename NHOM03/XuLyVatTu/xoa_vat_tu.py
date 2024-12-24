
# xoa_vat_tu.py
def xoa_thong_tin_vat_tu(ds_vat_tu, ma_vat_tu):
    """Xóa thông tin vật tư dựa trên mã vật tư."""
    for vat_tu in ds_vat_tu:
        if vat_tu["Ma vat tu"] == ma_vat_tu:
            ds_vat_tu.remove(vat_tu)
            print(f"Đã xóa vật tư: {ma_vat_tu}")
            return
    print("Không tìm thấy vật tư.")