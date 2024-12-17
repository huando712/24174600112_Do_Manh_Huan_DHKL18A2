# #Đọc ghi file

#C:\Users\Trung\Desktop\010100229802_Tran_Bao_Trung_DHKL18A2\file_a.txt
#file_a.txt
#file_upload\file_b.txt
open_file = open(file="file_a.txt", mode="r")
#r: chỉ đọc tệp tin từ dòng đầu đến dòng cuối, nếu tệp tin không tồn tại sẽ báo lỗi
#r+: đọc và ghi tệp tin từ dòng đầu đến dòng cuối, nếu tệp tin không tồn tại sẽ báo lỗi
#w: mở và ghi tệp tin (ghi đè), nếu tệp tin không tồn tại, tạo tệp tin mới
#w+: đọc và ghi tệp tin (ghi đè), nếu tệp tin không tồn tại, tạo tệp tin mới
#a: mở và ghi vào cuối tệp tin, nếu tệp tin không tồn tại báo lỗi
#a+: đọc và ghi vào cuối tệp tin, nếu tệp tin không tồn tại báo lỗi
# print(open_file.readline(),end="")
# print(open_file.readline(),end="")
# print(open_file.readline(),end="")
print(open_file.readlines())
open_file.close()

write_file = open(file="file_a.txt", mode="w")
# write_file.write("chuoi thong tin moi")
write_file.writelines(["dong 1\n", "dong 2\n", "dong 3"])
write_file.close()


with open(file="file_a.txt", mode="r") as open_file:
    list_text = open_file.readlines()

print(list_text)
for i in list_text:
    print(i)

list_text_copy = list_text.copy()
list_text_copy.append("dong 4\n")
list_text_copy.append("dong 5\n")
list_text_copy.append("dong 6\n")
list_text_copy[2] = "dong 3\n"
with open(file="file_a.txt", mode="w") as write_file:
    write_file.writelines(list_text_copy)
    


import csv
with open(file="book.csv", mode="r") as open_file:
    csv_reader = csv.reader(open_file,delimiter=",")
    csv_file = list(csv_reader).copy()


for row in csv_file:
    print(row)

with open(file="book.csv", mode="w") as write_file:
    csv_writer = csv.writer(write_file)
    csv_writer.writerows([['python', '300', '1200$'],
                          ['c++', '200', '2400$'],
                          ['java', '350', '200$'],
                          ['pascal', '10', '1$']])

import csv
with open(file="book.csv", mode="r") as open_file:
    csv_reader = csv.DictReader(open_file)
    list_file = list(csv_reader).copy()

for row in list_file:
    print(row)

with open(file="book.csv", mode="w") as write_file:
    csv_writer = csv.DictWriter(write_file,fieldname=["ten", "so_trang", "gia"])
    csv_writer.writeheader()
    csv_writer.writerow({"ten": "python",
                         "so_trang": 400,
                         "gia": "1200$"})
    csv_writer.writerows([{"ten": "python",
                         "so_trang": 400,
                         "gia": "1200$"},
                          {"ten": "python",
                         "so_trang": 400,
                         "gia": "1200$"},
                          {"ten": "python",
                         "so_trang": 400,
                         "gia": "1200$"},
                          {"ten": "python",
                         "so_trang": 400,
                         "gia": "1200$"}])
    