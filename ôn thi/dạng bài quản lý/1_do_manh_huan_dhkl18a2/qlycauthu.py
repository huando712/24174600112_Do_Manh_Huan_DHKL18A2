
import libs.xu_ly_thong_tin as p



print("=== MENU CHƯƠNG TRÌNH ===")
print("1. Đọc file danh sách cầu thủ")
print("2. Lưu file danh sách cầu thủ")
print("3. Nhập thông tin cầu thủ")
print("4. sửa thông tin cầu thủ")
print("5, danh sách cầu thủ")
print("6. cầu thủ giỏi nhất")
print("0. Thoát")
list_cauthu = []
while True:
    try:
        choice = int(input("Nhập vào lựa chọn: "))
    except:
        print("Lỗi: Vui lòng nhập một số nguyên!")

    else:
        if choice == 1:
         print("Đọc file...")
         p.doc_file(list_cauthu)
        elif choice == 2:
         print("Lưu file...")
         p.luu_file(list_cauthu)
        elif choice == 3:
         print("Nhập thông tin cầu thủ...")
         p.nhap_thong_tin(list_cauthu)
        elif choice ==4:
         print("thực hiện chỉnh sửa")
         p.sua_thong_tin(list_cauthu)
        elif choice == 5:
           print("thuc hien")
           p.in_danh_sach_theo_ma_cau_thu_sort(list_cauthu)
        elif choice==6:
           print("thuc hien")
           p.cau_thu_gioi(list_cauthu)
        
        else:
           print("thoat ctrinh")
           break
        
    
                
                



