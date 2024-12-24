# sua_vat_tu.py
def chinh_sua_thong_tin_vat_tu(ds_vat_tu, ma_vat_tu, **kwargs):
    """Chỉnh sửa thông tin của một vật tư dựa trên mã vật tư."""
    for vat_tu in ds_vat_tu:
        if vat_tu["Ma vat tu"] == ma_vat_tu:
            for key, value in kwargs.items():
                if key in vat_tu:
                    vat_tu[key] = value
            print(f"Đã cập nhật vật tư: {vat_tu}")
            return
    print("Không tìm thấy vật tư.")
