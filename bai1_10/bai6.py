#menu phim
print("chào mừng bạn đến rạp chiếu phim ABC")
print("vui lòng chọn phim bạn muốn xem")
print("1: phim tình cảm")
print("2: phim kinh dị")
print("3: phim hoạt hình")
print("4: phim khoa học viễn tưởng")
#nhập lưa chọn
lua_chon = float(input("nhập bộ phim bạn muốn lựa chọn (1->4):"))
if lua_chon == 1:
    print("phim tình cảm")
elif lua_chon == 2:
    print("phim kinh dị")
elif lua_chon == 3:
    print("phim hoạt hình")
elif lua_chon == 4:
    print("phim khoa học viễn tưởng")
else:
    print("lựa chọn không hợp lệ. Vui lòng chọn lại")    
