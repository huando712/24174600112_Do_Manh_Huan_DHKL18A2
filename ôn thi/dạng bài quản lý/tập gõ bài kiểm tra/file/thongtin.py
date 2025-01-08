import csv
def doc(hang_hoa: list):
    hang_hoa.clear()
    with open(file="csv\ds.csv", mode="r") as open_file:
        csv_reader=csv.reader(open_file)
        for item in csv_reader:
            print(item)
            hang_hoa.append(item)
def luu(hang_hoa: list):
    with open(file="csv\ds.csv", mode="w") as open_file:
        csv_writer=csv.writer(open_file)
        for item in hang_hoa:
            csv_writer.writerows(item)
            
def nhap_thong_tin(hang_hoa: list):
    while True:
        try:
            ma_hang=input("nhập vào mã hàng:")
            ten_hang=input("nhập vào tên hàng:")
            don_vi=input("nhập vào đơn vị tính:")
            so_luong=int(input("nhập vào số lượng:"))
            don_gia=int(input("nhập vào giá:"))
            assert so_luong>=0, "nhap sai"
            thanh_tien=don_gia*so_luong
            thue_vat=thanh_tien*0.1
            
            
            hang_hoa.append([
                ma_hang, ten_hang, don_vi, so_luong, don_gia, thanh_tien, thue_vat
                ])
            print("nhập thành công")
            break
        except:
            print("nhập sai")
def xem_danh_sach(hang_hoa: list):
    if not hang_hoa:
        print("danh sách trống")
        return
    hang_hoa.sort(key=lambda hang_hoa:hang_hoa[0])
    for xem in hang_hoa:
        print(f"mã hàng:{xem[0]}, tên hàng:{xem[1]}, đơn vị:{xem[2]}, số lương:{xem[3]}, đơn giá{xem[4]}, thành tiền{xem[5]}, thuế{xem[6]}")
def sua(hang_hoa:list):
    ma= input("nhập vào mã để sửa")
    vi_tri=-1
    for i,xem in enumerate(hang_hoa):
        if ma==xem[0]:
            vi_tri=i
            break
    if vi_tri==-1:
        print("không tìm thấy")
        return
    while True:
            try:
                ma_hang_moi=input("nhập vào mã hàng mới:")
                ten_hang_moi=input("nhập vào tên hàng mới:")
                don_vi_moi=input("nhập vào đơn vị tính mới:")
                so_luong_moi=int(input("nhập vào số lượng mới:"))
                don_gia_moi=int(input("nhập vào giá mới:"))
                assert so_luong_moi>=0, "nhap sai"
                thanh_tien=don_gia_moi*so_luong_moi
                thue_vat=thanh_tien*0.1
                
                
                hang_hoa[vi_tri]=[
                    ma_hang_moi, ten_hang_moi, don_vi_moi, so_luong_moi, don_gia_moi, thanh_tien, thue_vat
                ]
                print("sửa thành công")
                break
            except:
                print("nhập sai")
def xoa(hang_hoa:list):
    ma=("nhập mã hàng hóa")
    for xem in hang_hoa:
        if ma==hang_hoa[0]:
            hang_hoa.remove(xem)
            print(f"cầu thủ với mã {ma} đã được xóa")
            return
            