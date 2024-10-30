#bai 1
#nhập năm 
year = int(input("nhập năm: "))
#điều kiện  Năm nhuận chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
if year %4 ==0  and year %100 !=0 or year %400 ==0:
    print(" là năm nhuận")
else:
    print("không phải năm nhuận, vui lòng nhập lại")
