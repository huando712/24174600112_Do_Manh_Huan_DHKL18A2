#bài 1 viết hàm kiểm tra chuỗi kí tự có phải số nguyên
def tao_ham(n):
    """
    Kiểm tra chuỗi có phải là số nguyên không.
    : "n": Chuỗi ký tự
    :return: True nếu là số nguyên, False nếu không
    : isdigit kiểm tra chuỗi kí tự là số hay k
    :s.startswith("-") and s[1:].isdigit(): Kiểm tra nếu chuỗi bắt đầu bằng dấu - và phần còn lại là số (dành cho số nguyên âm)
    """
   
    if n.isdigit() or (n.startswith("-") and n[1:].isdigit()):
        return True
    return False
print(tao_ham("2"))
print(tao_ham("123"))
print(tao_ham("1"))
print(tao_ham("abc"))
print(tao_ham("-1"))

#bài 2 viết hàm kiểm tra chuỗi phải số nguyên dương
def tao_ham(n):
    if n.isdigit():
        if int(n) > 0:
            return True
        return False
    print(tao_ham("123"))
    print(tao_ham("abc"))
    print(tao_ham("-1"))      
#bài 3 viết hàm kiểm tra phải số thực hay không #số thực là số lẻ số thập phân
"""
    Kiểm tra chuỗi có phải là số thực hay không.
    :param s: Chuỗi ký tự
    :return: True nếu là số thực, False nếu không
    """
def tao_ham(n):
     if not n:  # Kiểm tra chuỗi rỗng
        return False
        if n[0 ]== '-': #kiểm tra dấu âm 
            n=n[1:] #loại bỏ dấu âm để kiểm tra phần còn lại
        if '.' in s:  # Kiểm tra nếu có dấu chấm (số thập phân)
          parts = s.split('.')  # Tách chuỗi thành 2 phần trước và sau dấu chấm
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return True
     elif n.isdigit():  # Kiểm tra nếu là số nguyên
        return True

     return False
print(tao_ham("1.5"))
print(tao_ham("56.7"))
print(tao_ham("123"))
print(tao_ham("abc"))
#bài 4 viết hàm kiểm tra phải số nguyên tố hay không
def tao_ham(s):
    if not isinstance(s, int):
        return False
    if s <= 1: #số nguyên tố phải là số lớn hơn 1
        return False
        for i in range(1, n+1):
            if n % i == 0:
                return False #nếu chia hết thì k là số nguyên tố
        return True #nếu k chia hêts là số nguyên tố
print(tao_ham("12"))    
print(tao_ham("abc"))    
#bài 5 viết hàm kiểm tra phải số chính phương hay không
import math

def is_perfect_square(n):
    """
    Kiểm tra xem số n có phải là số chính phương không.
    :param n: Số nguyên
    :return: True nếu là số chính phương, False nếu không
    """
    if n < 0:  # Số chính phương không thể là số âm
        return False
    sqrt_n = math.isqrt(n)  # Tính căn bậc 2 của n và làm tròn xuống
    return sqrt_n * sqrt_n == n  # Kiểm tra xem căn bậc 2 có bình phương bằng n không
print(is_perfect_square(16))   # True (4 * 4 = 16)
print(is_perfect_square(25))   # True (5 * 5 = 25)
print(is_perfect_square(20))   # False
print(is_perfect_square(1))    # True (1 * 1 = 1)
print(is_perfect_square(0))    # True (0 * 0 = 0)
print(is_perfect_square(-4))   # False (số âm không phải số chính phương)
#bài 6 viết hàm kiểm tra phải số hoàn hảo hay không

def so_hoan_hao(n):
    """
    : kiểm tra số hoàn hảo nguyên dương
    :n : số nguyên dương cần kiểm tra
    trả về TRue False
    """
    if n <= 1:
        return False #số hòan hảo phải là số nguyên dương
    tong = 0
    for i in range (1, n//2+1):
        if n % i == 0:
            tong+=1
            return tong == n
        # Ví dụ sử dụng
n = 28
if so_hoan_hao(n):
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")
#bài 7 viết hàm của ước chug lớn nhất của hai số nguyên bất kì
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
#bài 8