def gcd(a, b):
    """
    Tính ước chung lớn nhất (ƯCLN) của hai số nguyên a và b bằng thuật toán Euclid.
    Các bước:
    1 khởi đầu a b
    2 tính phần dư r=a%b
    3 cập nhập a<-b b<- r
    4 lặp lại cho đến khi b=0
    5 gias trị còn lại của a là ucln

    Tham số:
        a (int): Số nguyên thứ nhất.
        b (int): Số nguyên thứ hai.

    Trả về:
        int: Giá trị ƯCLN của a và b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Ví dụ sử dụng
a = 56
b = 98
print(f"ƯCLN của {a} và {b} là: {gcd(a, b)}")
"""
ví dụ minh họa:
Tìm ƯCLN của a=56 b=98
bước 1 :r=98%56 = 42
       :cập nhập a=56 b =42
bước 2 :r=56%42=14
        :cập nhập a=42 b=14
bước 3 :a=42 b=14
       :r= 56%14= 0  
       :cập nhập a =14 b =0
        :khi b=0 thuật toán dừng ucln a=14
"""                       