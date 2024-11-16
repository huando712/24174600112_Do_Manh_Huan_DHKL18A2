#bài 3 xóa các khoảng trống thừa chong chuỗi
#ví dụ ".........chuoi    nhap  vao...."
#cách 1 
chuoi_nhap_vao = input("nhap vao chuoi ky tu:")
tach_chuoi=chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
print(f"chuoi ket qua: {chuoi_ket_qua}")
#cach 2

chuoi_nhap = input("nhap vao chuoi")
ket_qua = ""
khoang_trang_lien_tiep = False

for ky_tu in chuoi_nhap:
    if ky_tu == ".":
        continue  # Bỏ qua các dấu chấm
    if ky_tu == " ":
        if not khoang_trang_lien_tiep:
            ket_qua += " "  # Chỉ thêm một khoảng trắng nếu trước đó chưa có khoảng trắng
            khoang_trang_lien_tiep = True
    else:
        ket_qua += ky_tu  # Thêm ký tự vào chuỗi kết quả
        khoang_trang_lien_tiep = False

# Loại bỏ khoảng trắng ở đầu
vi_tri_bat_dau = 0
while vi_tri_bat_dau < len(ket_qua) and ket_qua[vi_tri_bat_dau] == " ":
    vi_tri_bat_dau += 1

# Loại bỏ khoảng trắng ở cuối
vi_tri_ket_thuc = len(ket_qua) - 1
while vi_tri_ket_thuc >= 0 and ket_qua[vi_tri_ket_thuc] == " ":
    vi_tri_ket_thuc -= 1

# Cắt chuỗi để chỉ lấy phần không có khoảng trắng thừa
ket_qua = ket_qua[vi_tri_bat_dau:vi_tri_ket_thuc + 1]

print(ket_qua)  # Output: "chuoi nhap vao"