#s1
tong_s1 = 0
n = int(input("nhap vao gia tri nguyen duong :"))
for i in range(n+1):
  tong_s1 = tong_s1 + i
  if i > 0:
   print(f"tong cac so tu nhien : {tong_s1}")
#s2
tich_s2=1
n = int(input("nhap vao gia tri nguyen duong :"))
for i in range(n-1):
  if i >0:
   tich_s2 = tich_s2 * i
  print(f"tich cac so tu nhien : {tich_s2}")