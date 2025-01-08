import csv
def doc(list_cathu: list):
    list_cathu.clear()
    with open(file="file\ds.csv", mode= "r") as open_file:
       csv_reader=csv.reader(open_file)
       for item in csv_reader:
           print(item)
           list_cathu.append(item)

def luu(list_cauthu: list):
    with open(file="file\ds.csv", mode="w") as open_file:
        csv_writer=csv.writer(open_file)
        for item in list_cauthu:
            csv_writer.writerows(item)
def nhap_thong_tin(list_cauthu: list):
    while True:
        try:
            ma=input("nhập vào mã cầu thủ:")
            ten=input("nhập vào tên cầu thủ:")
            tuoi=int(input("nhap vao tuoi cau thu:"))
            assert tuoi >0, "nhap sai "
            vi_tri=input("nhap vao vi tri:")
            assert vi_tri in ["thu mon", "hau ve", "tien dao", "tien ve"], "nhap sai "
            so_huy_chuong=int(input("nhập vào số huy chương:"))
            if so_huy_chuong>10:
                thuong=so_huy_chuong*500000
            elif so_huy_chuong >=5:
                thuong=so_huy_chuong*300000
            elif so_huy_chuong >=1:
                thuong=so_huy_chuong*200000
            else:
                thuong=0.0
                
           
            list_cauthu.append([ma, ten, tuoi, vi_tri, so_huy_chuong, thuong])
            print("nhập thành công")
            break
        except:
            print("loi")

def sua_thong_tin(list_cauthu: list):
    ma=int(input("nhap vao ma cau thu"))
    vi_tri_ct= -1
    for i, cau_thu in enumerate(list_cauthu):
        if ma==cau_thu[0]:
            vi_tri_ct=i
            break
    if vi_tri_ct==-1:
        print("không tìm thấy")
        return
    
    while True:
                try:
                    ma=input("nhập vào mã cầu thủ:")
                    ten=input("nhập vào tên cầu thủ:")
                    tuoi=int(input("nhap vao tuoi cau thu:"))
                    assert tuoi >0, "nhap sai "
                    vi_tri=input("nhap vao vi tri:")
                    assert vi_tri in ["thu mon", "hau ve", "tien dao", "tien ve"], "nhap sai "
                    so_huy_chuong=int(input("nhập vào số huy chương:"))
                    if so_huy_chuong>10:
                        thuong=so_huy_chuong*500000
                    elif so_huy_chuong >=5:
                        thuong=so_huy_chuong*300000
                    elif so_huy_chuong >=1:
                        thuong=so_huy_chuong*200000
                    else:
                        thuong=0.0
                        
                
                    list_cauthu[vi_tri_ct]=[ma, ten, tuoi, vi_tri, so_huy_chuong, thuong]
                    print("nhập thành công")
                    break
                except:
                    print("loi")
#sắp xếp
def in_ra(list_cauthu: list):
    if not list_cauthu:
        print("danh sach trống")
        return
    list_cauthu.sort(key=lambda cau_thu: cau_thu[0])
    for cau_thu in list_cauthu:
     print(f"Mã: {cau_thu[0]}, Tên: {cau_thu[1]}, Tuổi: {cau_thu[2]}, Vị trí: {cau_thu[3]}, Số huy chương: {cau_thu[4]}, Thưởng: {cau_thu[5]}")
#xóa
def xoa_cau_thu(list_cauthu: list):
    ma = input("Nhập vào mã cầu thủ cần xóa: ")
    for cau_thu in list_cauthu:
        if cau_thu[0] == ma:  # Kiểm tra mã cầu thủ
            list_cauthu.remove(cau_thu)  # Xóa cầu thủ khỏi danh sách
            print(f"Cầu thủ với mã {ma} đã được xóa.")
            return
    print("Không tìm thấy cầu thủ với mã này.")
#in ra cầu thủ có tuổi nhỏ hơn 20    
def in_ra_tuoi(list_cauthu: list):
    if not list_cauthu:
        print("danh sach trống")
        return
    list_cauthu = [cau_thu for cau_thu in list_cauthu if cau_thu[2] < 20]
    if not list_cauthu:
        print("Không có cầu thủ nào dưới 20 tuổi.")
        return

    for cau_thu in list_cauthu:
        print(f"Mã: {cau_thu[0]}, Tên: {cau_thu[1]}, Tuổi: {cau_thu[2]}, Vị trí: {cau_thu[3]}, Số huy chương: {cau_thu[4]}, Thưởng: {cau_thu[5]}")
#cầu thủ có bàn thắng nhiều nhất


   


        


