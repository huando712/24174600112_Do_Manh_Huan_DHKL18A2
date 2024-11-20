# #Khởi tạo một danh sách
a = []
b = ["abc", 1, 5, 6.7, []]

a = 5
b = a
b = a + 1
print(a)
print(b)

#  Bộ nhớ của list được chia sẻ cho nhau
a = ["abc", "def", "ghijk", 1, 2, 3]
b = a
b[0] = "chuoi thay doi"
print(a)
print(b)

 #Phương thức sao lưu
a = ["abc", "def", "ghijk", 1, 2, 3]
b = a.copy()
b[0] = "chuoi thay doi"
print(a)
print(b)


# #thay đổi giá trị trong danh sách
a = ["abc", "def", "ghijk", 1, 2, 3]
a[3] = 10
a[1:4] = [6,7,8]
print(a)
# #độ dài của danh sách
print(len(a))
# #Các phương thức
# #Phương thức thêm và bớt
# # Thêm vào cuối danh sách
a.append("abca")
a.append([1,2,3])
print(a)
# #Thêm nhiều phần tử vào danh sách
a.extend([1,2,3])
print(a)
# #Xóa tất cả các phần tử trong danh sách
a.clear()
# #Lấy phần tử cuối cùng ra khỏi danh sách sử dung và xóa nó khỏi danh sách
b = a.pop()
print(a)
print(b)
# #Xóa một phần tử trong chuỗi
a.remove("abc")
# #Thêm 1 phần tử vào vị trí index
a.insert(3, "kkk")

# #Đếm số lần phần tử xuất hiện
a.count("abc")
# #Đảo ngược danh sách
a.reverse()
# #Trả về vị trí xuất hiện đầu tiên của phần tử trong danh sách
a.index(1)
# #Sắp xếp danh sách
a.sort(reverse=True)


b =[[1,2,[4,5,6]],"abc",[3,"rts",5]]
print(b[0][2][1])

# #Bài tập xử lý ma trận
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#Nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

print(matrix_a)

#Yêu cầu về nhà:

#Thực hiện các phép tính cơ bản của ma trận với số và của ma trận với ma trận





