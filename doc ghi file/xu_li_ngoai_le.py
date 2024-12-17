#Exception built-in

# Exception
# AssertionError

#Tự nghiên cứu
# raise
n = input("Nhap gia tri n: ")
if n.isdigit() == False:
    raise ValueError("loi nhap vao! yeu cau nhap vao so tu nhien")
# assert

k = 20
assert k > 10, "loi nhap vao! yeu cau nhap so > 10"
#Tự nghiên cứu
#try - except - else - finally
try:
    #Lệnh chạy thử
    k = 77777777
    n = input("Nhap gia tri n: ")
    n = int(n)
    assert n > 10, "loi nhap vao! yeu cau nhap so > 10"
    k = n
except ValueError:
    #Hoạt động nếu xảy ra lỗi
    print("loi nhap vao! yeu cau nhap vao so tu nhien")
#Có thể thêm bao nhiều except cũng được
except AssertionError as e:
    print(e)
else:
    #Hoạt động nếu không có lỗi xảy ra
    print(f"Gia tri nhap vao la {n}")
finally:
    #Hoạt động kể cả khi có lỗi hay không có lỗi
    print("Da thuc hien xong!")

#Các giá trị xử lý trong try - except đều có thể sử dụng kể cả khi có lỗi xảy ra
print("Gia tri n la: ", k)