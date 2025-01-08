#doc file ds cau thu
import csv
def doc_file(list_cauthu: list):
    list_cauthu.clear()
    with open(file="files\ds_cauthu.csv", mode="r") as open_file:
        csv_reader=csv.reader(open_file)
        for item in csv_reader:
            print(item)
            list_cauthu.append(item)
#luu file
def luu_file(list_cauthu: list):
    with open(file="files\ds_cauthu.csv", mode="w") as open_file:
        csv_writer=csv.writer(open_file)
        for item in list_cauthu:
            csv_writer.writerows(item)       
            

def nhap_thong_tin(list_cauthu: list):
    while True:
        try:
            # Nhập thông tin
            ma_cau_thu = input("Nhập mã cầu thủ: ")
            ten_cau_thu = input("Nhập tên cầu thủ: ")
            ten_doi_bong = input("Nhập tên đội bóng: ")
            
            tuoi = int(input("Nhập tuổi cầu thủ: "))
            assert tuoi > 0, "Tuổi phải lớn hơn 0."
            
            vi_tri = input("Nhập vị trí (thu mon, hau ve, tien ve, tien dao): ")
            assert vi_tri in ["thu mon", "hau ve", "tien ve", "tien dao"], "nhập sai"
            
            so_ban_thang = int(input("Nhập số bàn thắng: "))
            assert so_ban_thang >= 0, "Số bàn thắng không được âm."
            
            # Tính thưởng và trợ cấp
            if so_ban_thang > 10:
                thuong = so_ban_thang * 500000
                tro_cap = 0.1
            elif so_ban_thang >= 5:
                thuong = so_ban_thang * 300000
                tro_cap = 0.2
            elif so_ban_thang >= 1:
                thuong = so_ban_thang * 200000
                tro_cap = 0.3
            else:
                thuong = 0.0
                tro_cap = 0.0
            
            # Tính lương cơ bản theo vị trí
            if vi_tri == "thu mon":
                luong_vi_tri = 500000
            elif vi_tri == "hau ve":
                luong_vi_tri = 700000
            elif vi_tri == "tien ve":
                luong_vi_tri = 900000
            elif vi_tri == "tien dao":
                luong_vi_tri = 1000000
            
            # Tổng lương
            luong = luong_vi_tri + luong_vi_tri * tro_cap + thuong
            
            # Thêm vào danh sách
            list_cauthu.append([
                ma_cau_thu, ten_cau_thu, ten_doi_bong, tuoi, vi_tri, so_ban_thang, thuong, luong, tro_cap
            ])
            
            print("Thêm cầu thủ thành công!")
            break  # Kết thúc vòng lặp khi thành công

        except:
            print(f"Lỗi: ")
# def sua_thong_tin(list_cauthu:list):
#     ma_cau_thu = input("nhập vào mã cầu thủ")
#     vi_tri_ct=-1
#     for i in range(list_cauthu):
#         if ma_cau_thu==list_cauthu[i][0]:
#             vi_tri_ct=i
#             break
#         if vi_tri_ct == -1:
#             print("cầu thủ không tồn tại")
#         else:
#             while True:
#                 try:
#                     # Nhập thông tin
#                     ma_cau_thu = input("Nhập mã cầu thủ: ")
#                     ten_cau_thu = input("Nhập tên cầu thủ: ")
#                     ten_doi_bong = input("Nhập tên đội bóng: ")
                    
#                     tuoi = int(input("Nhập tuổi cầu thủ: "))
#                     assert tuoi > 0, "Tuổi phải lớn hơn 0."
                    
#                     vi_tri = input("Nhập vị trí (thu mon, hau ve, tien ve, tien dao): ")
#                     assert vi_tri in ["thu mon", "hau ve", "tien ve", "tien dao"], "nhập sai"
                    
#                     so_ban_thang = int(input("Nhập số bàn thắng: "))
#                     assert so_ban_thang >= 0, "Số bàn thắng không được âm."
                    
#                     # Tính thưởng và trợ cấp
#                     if so_ban_thang > 10:
#                         thuong = so_ban_thang * 500000
#                         tro_cap = 0.1
#                     elif so_ban_thang >= 5:
#                         thuong = so_ban_thang * 300000
#                         tro_cap = 0.2
#                     elif so_ban_thang >= 1:
#                         thuong = so_ban_thang * 200000
#                         tro_cap = 0.3
#                     else:
#                         thuong = 0.0
#                         tro_cap = 0.0
                    
#                     # Tính lương cơ bản theo vị trí
#                     if vi_tri == "thu mon":
#                         luong_vi_tri = 500000
#                     elif vi_tri == "hau ve":
#                         luong_vi_tri = 700000
#                     elif vi_tri == "tien ve":
#                         luong_vi_tri = 900000
#                     elif vi_tri == "tien dao":
#                         luong_vi_tri = 1000000
                    
#                     # Tổng lương
#                     luong = luong_vi_tri + luong_vi_tri * tro_cap + thuong
                    
#                     # Thêm vào danh sách
#                     list_cauthu[vi_tri_ct]=[
#                         ma_cau_thu, ten_cau_thu, ten_doi_bong, tuoi, vi_tri, so_ban_thang, thuong, luong, tro_cap
#                     ]
                    
#                     print("sửa thành công!")
#                     break  # Kết thúc vòng lặp khi thành công

#                 except:
#                       print(f"Lỗi: ")
def sua_thong_tin(list_cauthu: list):
    ma_cau_thu = input("Nhập vào mã cầu thủ: ")
    vi_tri_ct = -1

    # Tìm vị trí cầu thủ cần sửa
    for i, cau_thu in enumerate(list_cauthu):  # Sử dụng enumerate
        if ma_cau_thu == cau_thu[0]:  # So sánh mã cầu thủ
            vi_tri_ct = i
            break

    # Nếu không tìm thấy cầu thủ
    if vi_tri_ct == -1:
        print("Cầu thủ không tồn tại.")
        return

    # Sửa thông tin cầu thủ
    while True:
        try:
            # Nhập thông tin
            ma_cau_thu_moi = input("Nhập mã cầu thủ mới: ")
            ten_cau_thu = input("Nhập tên cầu thủ: ")
            ten_doi_bong = input("Nhập tên đội bóng: ")
            
            tuoi = int(input("Nhập tuổi cầu thủ: "))
            assert tuoi > 0, "Tuổi phải lớn hơn 0."
            
            vi_tri = input("Nhập vị trí (thu mon, hau ve, tien ve, tien dao): ")
            assert vi_tri in ["thu mon", "hau ve", "tien ve", "tien dao"], "Nhập sai vị trí."

            so_ban_thang = int(input("Nhập số bàn thắng: "))
            assert so_ban_thang >= 0, "Số bàn thắng không được âm."

            # Tính thưởng và trợ cấp
            if so_ban_thang > 10:
                thuong = so_ban_thang * 500000
                tro_cap = 0.1
            elif so_ban_thang >= 5:
                thuong = so_ban_thang * 300000
                tro_cap = 0.2
            elif so_ban_thang >= 1:
                thuong = so_ban_thang * 200000
                tro_cap = 0.3
            else:
                thuong = 0.0
                tro_cap = 0.0

            # Tính lương cơ bản theo vị trí
            if vi_tri == "thu mon":
                luong_vi_tri = 500000
            elif vi_tri == "hau ve":
                luong_vi_tri = 700000
            elif vi_tri == "tien ve":
                luong_vi_tri = 900000
            elif vi_tri == "tien dao":
                luong_vi_tri = 1000000

            # Tổng lương
            luong = luong_vi_tri + luong_vi_tri * tro_cap + thuong

            # Cập nhật thông tin cầu thủ
            list_cauthu[vi_tri_ct] = [
                ma_cau_thu_moi, ten_cau_thu, ten_doi_bong, tuoi, vi_tri, so_ban_thang, thuong, luong, tro_cap
            ]

            print("Sửa thông tin cầu thủ thành công!")
            break  # Kết thúc vòng lặp khi thành công
        except:
            print("nhap sai")

def in_danh_sach_theo_ma_cau_thu_sort(list_cauthu: list):
    if not list_cauthu:  # Kiểm tra danh sách rỗng
        print("Danh sách cầu thủ hiện đang trống.")
        return

    # Sắp xếp danh sách tại chỗ (không trả về danh sách mới)
    list_cauthu.sort(key=lambda cau_thu: cau_thu[0])

    # In ra
    for cau_thu in list_cauthu:
        print(f"mã cầu thủ:{cau_thu[0]},tên cầu thủ:{cau_thu[1]}, ten_doi_bong:{cau_thu[2]}, tuoi:{cau_thu[3]}, vi_tri:{cau_thu[4]}, so_ban_thang:{cau_thu[5]}, thuong{cau_thu[6]}, luong{cau_thu[7]}, tro_cap{cau_thu[8]} ")

#bàn thắng
def cau_thu_gioi(list_cauthu:list):
    if not list_cauthu:
        print("không có cauaaf thủ nào")
        return 
    cau_thu_gioi=max(list_cauthu, Key=lambda cau_thu: cau_thu[5])
    for cau_thu in list_cauthu:
        print(f"mã cầu thủ:{cau_thu_gioi[0]},tên cầu thủ:{cau_thu_gioi[1]}, ten_doi_bong:{cau_thu_gioi[2]}, tuoi:{cau_thu[3]}, vi_tri:{cau_thu_gioi[4]}, so_ban_thang:{cau_thu_gioi[5]}, thuong{cau_thu_gioi[6]}, luong{cau_thu_gioi[7]}, tro_cap{cau_thu_gioi[8]} ")
# def in_ra_tuoi(list_cauthu: list):
#     if not list_cauthu:
#         print("danh sach trống")
#         return
#     list_cauthu = [cau_thu for cau_thu in list_cauthu if cau_thu[3] < 20]
#     if not list_cauthu:
#         print("Không có cầu thủ nào dưới 20 tuổi.")
#         return
#     for cau_thu in list_cauthu:
        
#         print(f"mã cầu thủ:{cau_thu[0]},tên cầu thủ:{cau_thu[1]}, ten_doi_bong:{cau_thu[2]}, tuoi:{cau_thu[3]}, vi_tri:{cau_thu[4]}, so_ban_thang:{cau_thu[5]}, thuong{cau_thu[6]}, luong{cau_thu[7]}, tro_cap{cau_thu[8]} ")



