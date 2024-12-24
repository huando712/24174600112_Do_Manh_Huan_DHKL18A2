# tim_kiem_vat_tu.py
def tim_kiem_thong_tin_vat_tu(ds_vat_tu, keyword):
    """Tìm kiếm thông tin vật tư dựa trên từ khóa."""
    ket_qua = [vat_tu for vat_tu in ds_vat_tu if keyword.lower() in str(vat_tu).lower()]
    if ket_qua:
        for vat_tu in ket_qua:
            print(vat_tu)
    else:
        print("Không tìm thấy kết quả phù hợp.")
