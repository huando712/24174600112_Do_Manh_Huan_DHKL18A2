#bài 4
# thông tin đề bài
U = 220 #hiệu điện thế (v)
I = 2.7 # cường độ dòng điện (A)
7000  # giá điện(kw/h)
#thời gian sử dụng điện
s = float(input("số giây sử dụng điện: "))
if s>0:
    print("số giây sử dụng không thể âm")
else:
    print(" số giây sử dụng không hợp lệ")
# tiền điện phải trả ( điện năng tiêu thụ*thời gian*giá điện)
#đổi giây ra giờ 
h = s/3600
print(f"số giờ điện đã dùng{h}")
dien_nang_tieu_thu = 220*2.7*h

tien_dien_phai_tra = dien_nang_tieu_thu*7000
print(f"số tiền điện phải trả là{tien_dien_phai_tra}vnđ")
