#bài 1
import math
# nhập bán kính(r) và chiều cao(h)
r = float(input("nhập bán kính khối trụ: "))
h = float(input("nhập chiều cao khối trụ: "))
# câu lệnh điều kiện kiểm tra cho bán  kinh và chiều cao
if h>0 and r>0:
   print(" bán kính hoặc chiều cao không được âm")
else:
   print("gia tri nhap khong thoa man")   

pi = 3.14
dtxq = 2*pi*r*h
dttp = 2 *pi*r*(r + h)
Vt = pi*r**2*h
#in ra kết quả
print(f"diện tích xung quanh: {dtxq:.2f}")
print(f"diện tích toàn phần: {dttp:.2f}")
print(f"thể tích: {Vt:.2f}")
print("kết thúc chương trình")












  


