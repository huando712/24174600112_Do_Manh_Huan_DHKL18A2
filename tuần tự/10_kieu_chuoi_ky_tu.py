print("hello world")
a= "hello world"
b= 'hello world'
c = 'bannj a nói:"abcd"'
d = "bạn a nói :'abcd'"
#kiểu dữ liệu tuần tự là kiểu dữ liệu có thể truy cập vào các phần tử ở trong nó
#truy cập sử dụng kiểu dữ liệu index(danh mục)
print(a[4])
#[start:stop:step]
#start:vị trí ban đầu
#stop; vị trí kết thúc
#step khoảng cách giữa các bước
print(a[1:7])#lấy các giá trị từ start đến stop -1
print(a[:7])
print(a[1:])
print(a[:])
#măcj định của step luôn luon =1
print(a[1:7:2])
print(a[1::2])
print(a[::2])
print(a[::])
print(a[::-1])
print(range(5))#0,1,2,3,4
#range cũng sử dụng start stop step
range(1,5,2)
for item in a:
    print(item)
    #hàm đo độ dài kiểu dữ liệu tuần tự len
print(len(a))
range(len(a))#thu dc chỉ mục chạy từ 0 đến len a
for i in range(len(a)):
    print(a[i])
#tính chất của kiểu dữ liệu kí tự
#có thể truy cập 
#k thể chỉnh sửa
#có thể sắp xepes
b = "hello world" + "world"
print(b)
c = ""
for i in range(len(a)):
    if a[i] == "a":
        c+=i
#các phương thức cử lí trong chuỗi kí tự
a = "hello world"
#các phương thc trả về cho mình trune or false
#các phương thuc này sẽ thường bắt đầu bằng is
# kiểm tra xem chuỗi có phải alpgnumberic(chỉ có ký tự số và chữ hay k)
print(a.isalnum())#kiểm tra  chỉ có kí tự chữ
#numberic kiểm tra chuỗi có tòn số
#chẩcter kiểm tra toàn chữ hay k
#isalpha
print(a.isascii())#số thông thường
print(a.isdecimal())#số thập phân
#kiểm tra xem chuỗi cs khoảng trống hay k
print(a.isspace())
#kiểm tra in hoa hay thường 
#issupport
#islower
#kiếm tra kí tự tồn tại tron chuỗi kí tự
print(a.find("11"))
print(a.count("1"))
#xóa kí tự đàu và cuỗi chuỗi kí tự
a.strip()
a_sua = a.istrip()
#rstrip
#thay thế kí tự bất kì
a_sua = a.replace("1","w")
