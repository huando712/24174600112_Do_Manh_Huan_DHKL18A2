# #set - Tập hợp trong pyhton
# #Tính chất của tập hợp
# #- Không có sắp xếp, không có thứ tự
# #- Những phần tử trong tập hợp là đặc hiệu (unique)
# #- Các giá trị trong set có thể thay đổi được tuy nhiên nó chỉ có thể chứa các phần tử 
# #mang giá trị không đổi

list_a = ["fol", "baa", "baal"]

set_a = {1,2,3,"abc"}
set_b = set(list_a) #=> {"fol", "baa", "baal"}

# #Kiểm tra số phần tử trong tập hợp
len(set_a)
# #Kiểm tra phần tử có tồn tại trong tập hợp không
2 in set_a #=> trả về kiểu dữ liệu boolean: True

if 2 in set_a:
 print("2 co trong tap hop")
    
2 not in set_a #=> trả về kiểu dữ liệu boolean: False

if 2 not in set_a:
 print("2 khong co trong tap hop")

# #Kiểm tra so sánh 2 tập hợp
# # tập hợp A
 tap_hop_a = {"a", "b", "c", "d"}
# # tập hợp B
tap_hop_b = {1, 2, 3, "a", "b"}

# #Kiểm tra tập A có phải tập con của tập hợp B hay không? 
tap_hop_a.issubset(tap_hop_b) #=> trả về kiểu dữ liệu boolean
tap_hop_a < tap_hop_b
tap_hop_a <= tap_hop_b

# #Kiểm tra tập hợp A có phải tập cha của tập hợp B hay không?
tap_hop_a.issuperset(tap_hop_b)
tap_hop_a > tap_hop_b
tap_hop_a >= tap_hop_b

# #Kiểm tra xem 2 tập họp có giao nhau hay không?
tap_hop_a.isdisjoint(tap_hop_b)#=> trả về True nếu không có phần tử chung và False nếu có

# #Các tính toán trong tập hợp
# # tập hợp A
tap_hop_a = {"a", "b", "c", "d"}
# # tập hợp B
tap_hop_b = {1, 2, 3, "a", "b"}
# # tập hợp C
tap_hop_c = {1,2,3,4,5,6}

# #Phép hợp các tập hợp
tap_hop_tong = tap_hop_a.union(tap_hop_b)
tap_hop_tong = tap_hop_a.union(tap_hop_b).union(tap_hop_c)
tap_hop_tong = tap_hop_a | tap_hop_b | tap_hop_c

# #Phép lấy phần giao giữa các tập hợp
tap_hop_giao = tap_hop_a.intersection(tap_hop_b)
tap_hop_giao = tap_hop_a.intersection(tap_hop_b).intersection(tap_hop_c)
tap_hop_giao = tap_hop_a & tap_hop_b & tap_hop_c

# #Phép lấy phần tử trong một tập hợp mà không có trong các tập hợp còn lại
tap_hop_khac = tap_hop_a.difference(tap_hop_b)
tap_hop_khac = tap_hop_a.difference(tap_hop_b).difference(tap_hop_c)
tap_hop_khac = tap_hop_a - tap_hop_b - tap_hop_c

# #Phép lấy hợp của các phần có trong tập hợp này mà không có trong tập hợp kia
tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b)
tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b).symmetric_difference(tap_hop_c)
tap_hop_khac_giao = tap_hop_a ^ tap_hop_b ^ tap_hop_c

# #Chỉnh sửa tập hợp
tap_hop_a = {1, 2, 3}
tap_hop_b = {"a","b","c"}
##Thêm phần tử vào a
# tap_hop_a.add(9)
# tap_hop_a.update([4,5,6]) #Tương tự với việc hợp 2 tập hợp
a = 1
b = 2
a += b
a = a + b
tap_hop_a = tap_hop_a | tap_hop_b
tap_hop_a |= tap_hop_b

# #Giữ lại các phần tử là giao của hai tập hợp
tap_hop_a.intersection_update(tap_hop_b)
tap_hop_a = tap_hop_a & tap_hop_b
tap_hop_a &= tap_hop_b

# #Giữ lại các phần tử có trong tập xét mà không có trong tập còn lại
tap_hop_a.difference_update(tap_hop_b)
tap_hop_a = tap_hop_a - tap_hop_b
tap_hop_a -= tap_hop_b

# #Giữ lại các phần tử không tồn tại trong cả hai tập hợp
tap_hop_a.symmetric_difference_update(tap_hop_b)
tap_hop_a = tap_hop_a ^ tap_hop_b
tap_hop_a ^= tap_hop_b

# #Xóa phần tử trong tập hợp
# #Xóa 1 phần tử
tap_hop_a.remove(2)
# #Xóa nhiều phần tử trong một tập hợp
tap_hop_a.difference_update({1,2})
# #Xóa phần tử không gây lỗi
tap_hop_a.discard(2)
# #Lấy 1 phần tử bất kì ra để sử dụng và xóa phần tử này khỏi tập hợp
tap_hop_a.pop()
# #Xóa toàn bộ tập hợp
tap_hop_a.clear()


tap_hop = {"a","b","c","d","e"}
while tap_hop:
    a = tap_hop.pop()
    print(a) 