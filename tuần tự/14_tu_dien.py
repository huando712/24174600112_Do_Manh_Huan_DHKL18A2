#Từ điển trong python
#- Lưu trữ các kiểu dữ liệu khác nhau
#- Có thể thay đổi các giá trị trong từ điển
#- Có thể lưu các kiểu dữ liệu tuần tự khác tạo thành mạng lưới
#- Không sử dụng chỉ mục mà thay vào đó là các khóa (key)
#- Tất cả các giá trị phải truy cập bằng khóa
tu_dien = {"abc":1,
           (0,1):"hijk", 
           3:[1,2,3]}
#Khai báo từ điển
#- Từ điển sử dụng ngoặc {} để khưởi tạo
#- Mỗi phần tử phải theo cặp khóa: giá trị
#- Khóa trong từ điển phải là không thể thay đổi
#- Khóa không được giống nhau
list_a = [(0, "Hoang"), (1, "Cuong"), (2, "Lam")]
tu_dien_a = dict(list_a)
#Từ điển trong Python có cách hoạt động giống như JSON


#Truy cập các phần tử trong từ điển
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["a"]
#Lấy tập hợp khóa
tap_hop_khoa = tu_dien.keys()
#Lấy danh sách giá trị
danh_sach_gia_tri = list(tu_dien.values())
#lấy danh sách các cặp khóa giá trị
danh_sach_khoa_gia_tri = list(tu_dien.items())

#Thêm giá trị vào trong từ điển
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}

tu_dien["d"] = 4

tu_dien.update({"e": 5, "f": 6, "g": 7})

#Xóa phần tử trong từ điển
tu_dien.clear() #Xóa toàn bộ các giá trị
tu_dien.pop("b") #Lấy ra và Xóa phần tử tại khóa 
tu_dien.popitem() #Lấy ra và xóa phần tử bất kì