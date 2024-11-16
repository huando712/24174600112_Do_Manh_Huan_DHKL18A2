#bài tập về chuỗi kí tự
#dậng thứ nhất áp dụng xử lí chuỗi vòng lặp v
#bài 1 nhập vào 1 chuỗi kí tự bất kì đếm số kí tự trong chuỗi
chuoi_nhap_vao = input("nhap vao chuoi bat ky")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"so ky tu trong chuoi {so_ky_tu_trong_chuoi}")
#cách 2
chuoi_nhap_vao = input("nhap vao chuoi ki tu")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem+=1
print(f"so ky tu trong chuoi {dem}")
#bài 2 nhập vào 1 chuỗi bất kì xóa các khoảng trống ở đầu và cuối chuỗi
#cách 1
chuoi_nhap_vao = input("nhap vao chuoi bat ky")
chuoi_da_xoa_khoang_trong =chuoi_nhap_vao.strip()
print(f"chuoi sau khi xoa khoang trong{chuoi_da_xoa_khoang_trong}")
#cách 2
chuoi_nhap_vao = input("nhap vao chuoi bat ky")
#chuoi nhap vao
chuoi_xu_ly_dau = ""
for chu in chuoi_nhap_vao:
    if chu == " " and Kiem_tra_dau == False:
        continue
    else:
        Kiem_tra_dau == True
        chuoi_xu_ly_dau+= chu

chuoi_dao_nguoc = chuoi_xu_ly_dau[:: -1]
for chu in chuoi_dao_nguoc:
    if chu == " " and Kiem_tra_dau == False:
        continue
    else:
        Kiem_tra_dau == True
        chuoi_dao_nguoc_xu_ly_dau= chuoi_dao_nguoc_xu_ly_dau + chu

chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[:: -1]
print(f"chuoi sau khi xoa {chuoi_ket_qua}")

#bài 3 xóa các khoảng trống thừa chong chuỗi
#ví dụ ".........chuoi    nhap  vao...."
#cachs 1
chuoi_nhap_vao = input("nhap vao chuoi bat ky:")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#chuoi nhap vao
print(f"chuoi ket qua: {chuoi_ket_qua}")
#cach 2 sử dungk chuỗi trên mà k sử dụng các phương thưc














#dạng thứ 2 áp dụng kết hợp xử lí vòng lặp và xử lý chuỗi kí tự
#bài 1
# đếm xem có bao nhiêu ký tự là chữ bao nhiêu ký tự và bao nhiêu kí tự đặc biệt
#ispalit( kiểm tra chứ)
#isdigit( kiểm tra số)
chuoi_nhap_vao = input("nhap vao chuoi bat ky:")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu += 1
    else:
        if chu.isdigit()== True:
            dem_so +=1
        else:
            dem_ky_tu_dac_biet+=1
print(f"so chu cai {dem_chu}")     
print(f"so so {dem_so}")
print(f"so ky tu dac biet{dem_ky_tu_dac_biet}")       




#bài 3 nhập vào 2 số thực bất kì tính tổng 2 só thực đó
while True:
 a = float(input("nhap vao so thuc a"))
 so_kiem_tra = a.replace(".","")
 so_kiem_tra = so_kiem_tra.replace("-","")
 if a.isdigit()== False:
    print("gia tri nhap vao khong phai gia tri so")
 else:
    dem_dau_cham = a.conut(".")
    dem_dau_gach = a.count("-")
    if dem_dau_cham > 1 of dem_dau_gach >1:
     print("gia tri nhap vao khong phai gia tri so")
else:
    vi_tri_dau_gach = a.find(".")
    if vi_tri_dau_gach !=0:
        print("gia tri nhap khong phai la so")
    else:
        break
        

a = float(a)
b = float(b)
tong = a+b
while True:
 b = float(input("nhap vao so thuc b"))


so_kiem_tra = a.replace(".","")
so_kiem_tra = so_kiem_tra.replace("-","")
if a.isdigit()== False:
    print("gia tri nhap vao khong phai gia tri so")
else:
    dem_dau_cham = a.conut(".")
    dem_dau_gach = a.count("-")
    if dem_dau_cham > 1 of dem_dau_gach >1:
     print("gia tri nhap vao khong phai gia tri so")
    else:
       vi_tri_dau_gach = a.find(".")
    if vi_tri_dau_gach !=0:
        print("gia tri nhap khong phai la so")
    else:
        
        break
