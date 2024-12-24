# xem_vat_tu.py

def xem_phong_kem_vat_tu(ds_vat_tu):
    """Hiển thị thông tin phòng kèm theo danh sách vật tư."""
    if not ds_vat_tu:
        print("Danh sách vật tư trống.")
        return

    print(f"{'Ma phong':<15}{'Tong so bo ban ghe':<20}{'Tong so man hinh':<20}{'Tong so dieu hoa':<20}{'So bo ban ghe hong':<20}{'So man hinh hong':<20}{'So dieu hoa hong':<20}{'Thang':<15}{'Nam':<15}{'Ma vat tu':<15}")
    for vat_tu in ds_vat_tu:
        print(f"{vat_tu['Ma phong']:<15}{vat_tu['Tong so bo ban ghe']:<20}{vat_tu['Tong so man hinh']:<20}{vat_tu['Tong so dieu hoa']:<20}{vat_tu['So bo ban ghe hong']:<20}{vat_tu['So man hinh hong']:<20}{vat_tu['So dieu hoa hong']:<20}{vat_tu['Thang']:<15}{vat_tu['Nam']:<15}{vat_tu['Ma vat tu']:<15}")
