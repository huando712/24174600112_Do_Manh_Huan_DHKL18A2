import libs.xu_ly_thong_tin_cau_thu as p
print("==menu chuong trinh==")
print("1. doc file csv")
print("2. nhap thong tin cau thu")
print("3. sua thong tin")
print("4. luu vao file csv")
print("5. thoat")
list_cauthu = []
while True:
    try:
        lua_chon=input("nhap lua chon:")
        lua_chon=int(lua_chon)
    except:
        print("nhap sai yeu cau nhap lai")
    else:
        if lua_chon == 1:
            print("thuc hien doc file")
            p.doc_file(list_cauthu)
        elif lua_chon ==2:
            print("thuc hien nhap thong tin cau thu")
            p.nhap_thong_tin(list_cauthu)
        elif lua_chon ==3:
            print("tuc hien sua")
            p.sua_thong_tin(list_cauthu)
        elif lua_chon == 4:
            print("thuc hien luu vao file csv")
            p.luu_file(list_cauthu)
        else:
            print("thoat chuong trinh")
            break

        

        
