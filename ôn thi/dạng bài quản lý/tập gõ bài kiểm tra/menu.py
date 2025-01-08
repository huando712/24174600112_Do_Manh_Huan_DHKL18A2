import file.thongtin as x1
print("===menu===")
print("1, doc file")
print("2. luu fife")
print("3. xem danh sách")
print("4. nhập thông tin")
print("5. sửa theo mã hàng hóa")
print("6. xóa theo mã")
print("7. sắp xếp theo tên hàng")
print("0. thoát")
hang_hoa =[]
while True:
    try:
        lua_chon=int(input("nhập vào lựa chọn"))
        
    except:
        print("nhập sai")
    else:
        if lua_chon ==1:
            print("thuc hien")
            x1.doc(hang_hoa)
        elif lua_chon ==2:
            print("thuc hien")
            x1.luu(hang_hoa)
        elif lua_chon==4:
            print("thuc hien")
            x1.nhap_thong_tin(hang_hoa)
        elif lua_chon==3:
            print("thuc hien")
            x1.xem_danh_sach(hang_hoa)
        elif lua_chon==5:
            print("thuc hien")
            x1.sua(hang_hoa)
        elif lua_chon ==6:
            print("thuc hien")
            x1.xoa(hang_hoa)
        elif lua_chon==7:
            print("thuc hien")
            x1.sap_xep_mat_hang(hang_hoa)
        else:
            print("thoát")
            break
            