import lis.xu_ly as p
print("=== menu chuong  trinh===")
print("1. doc file")
print("2: luu file")
print("3. nhap thong tin")
print("4. sua thong tin")
print("5. in ra ")
print("6 xóa cầu thủ")
print("0. thoat")

list_cauthu = []
while True:
    try:
        lua_chon = int(input("nhap vao lua chon"))
    except:
        print ("nhap sai")
    else:
        if lua_chon ==1:
            print("thuc hien doc file")
            p.doc(list_cauthu)
        elif lua_chon==2:
            print("thuc hien luu file")
            p.luu(list_cauthu)
        elif lua_chon ==3:
            print("thuc hien nhap")
            p.nhap_thong_tin(list_cauthu)
        elif lua_chon ==4:
            print("thuc hien sua thong tin")
            p.sua_thong_tin(list_cauthu)
        elif lua_chon==5:
            print("thuc hiện in ra")
            p.in_ra(list_cauthu)
        elif lua_chon==6:
            print("thực hiện chức năng")
            p.xoa_cau_thu(list_cauthu)
        else:
            print("thoát")
            break
        
            