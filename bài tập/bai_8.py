#bài 8
import math
# nhập giá trị
x = float(input("nhập giá trị vào phương trình:"))
# điều kiện log phải lớn hơn 0
if x > 0:
    print("giá trị của x phải lớn hơn 0")
else:
    print("giá trị không thỏa mãn")
#tính phương trình
log4x = math.log(x,4)
logx2 = math.log(2,x)
y=log4x+logx2
#tính đến số thập phân thứ 2
y_rounded = round(y , 2)
print(f"giá trị của phương trình là:{y_rounded}")

