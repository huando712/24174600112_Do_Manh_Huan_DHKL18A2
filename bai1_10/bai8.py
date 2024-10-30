# Nhập điểm của sinh viên
diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))

# Tính điểm trung bình với trọng số
diem_trung_binh = (diem_chuyen_can * 0.2) + (diem_giua_ky * 0.3) + (diem_cuoi_ky * 0.5)

# Xếp loại điểm theo quy tắc
if diem_trung_binh >= 9:
    loai = "A"
elif diem_trung_binh >= 7:
    loai = "B"
elif diem_trung_binh >= 5:
    loai = "C"
else:
    loai = "D"

# In kết quả
print("Điểm trung bình:", diem_trung_binh)
print("Xếp loại:", loai)