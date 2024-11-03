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
#s3
s3 = 0
n = int(input("nhap cac so nguyen duong"))
for i in range(1, n + 1):
  s3 += (-1)**(i + 1) / i

print(f"Tổng S3 đến n = {n} là: {s3}")
#s4
s4 = 0
n = int(input("nhap gia tri nguyen duong"))
for k in range(n):
  s_4 = s4 + k/(k+2)
  print(f"Tổng S4 đến k = {n} là: {s4}")
