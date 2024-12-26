def sap_xep_danh_sach(danh_sach, key):
    try:
        return sorted(danh_sach, key=lambda x: x.get(key, ""))
    except Exception as e:
        return f"Lỗi khi sắp xếp: {e}"
