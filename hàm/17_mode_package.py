
#Kiểm tra điều kiện số nguyên tố
# import module
# from mod_1 import *
# from mod_2 import *

#import package
from pkg.mod_1 import *
from pkg.mod_2 import *

n = int(input("Nhap vao so nguyen bat ki: "))
if kiem_tra_so_nguyen_to(n):
    print("Day la so nguyen to")
else:
    print("Day khong la so nguyen to")