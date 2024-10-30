# Nhập thông tin từ người dùng
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
khoang_cach = float(input("Nhập khoảng cách di chuyển (km): "))
time_doi = int(input("Nhập thời gian chờ (phút): "))

# Khởi tạo biến cước taxi
fare = 0

# Tính cước taxi theo loại xe
if loai_xe == 4:
    mở_cửa = 11000  # Giá mở cửa cho xe 4 chỗ
    khoang_cach_1 = 12100  # Từ 0.8 km đến 20 km
    khoang_cach_2 = 10000  # Từ km thứ 21 trở đi
    free_đợi_time = 5  # Thời gian chờ miễn phí
    tiền_chờ = 800  # Tiền chờ mỗi phút sau 5 phút

    # Tính cước mở cửa
    fare += mở_cửa

    # Tính cước theo khoảng cách
    if khoang_cach > 0.8:
        khoang_cach -= 0.8  # Khấu trừ khoảng cách mở cửa
        if khoang_cach <= 20 - 0.8:
            fare += khoang_cach * khoang_cach_1
        else:
            fare += (20 - 0.8) * khoang_cach_1
            fare += (khoang_cach - (20 - 0.8)) * khoang_cach_2

elif loai_xe == 7:
    mở_cửa = 13000  # Giá mở cửa cho xe 7 chỗ
    khoang_cach_1 = 14100  # Từ 0.8 km đến 30 km
    khoang_cach_1 = 12000  # Từ km thứ 31 trở đi
    free_đợi_time = 5  # Thời gian chờ miễn phí
    tiền_chờ = 800  # Tiền chờ mỗi phút sau 5 phút

    # Tính cước mở cửa
    fare += mở_cửa

    # Tính cước theo khoảng cách
    if khoang_cach > 0.8:
        khoang_cach -= 0.8  # Khấu trừ khoảng cách mở cửa
        if khoang_cach <= 30 - 0.8:
            fare += khoang_cach * khoang_cach_1
        else:
            fare += (30 - 0.8) * khoang_cach_1
            fare += (khoang_cach - (30 - 0.8)) * khoang_cach_2

else:
    print("Loại xe không hợp lệ.")
    fare = None  # Đặt fare là None nếu loại xe không hợp lệ

# Tính tiền chờ
if fare is not None:  # Chỉ tính tiền chờ nếu fare không phải là None
    if time_doi > free_đợi_time:
        time_doi -= free_đợi_time  # Khấu trừ thời gian miễn phí
        fare += time_doi * tiền_chờ  # Tính tiền chờ

    # In kết quả cước taxi
    print(f"Cước taxi: {fare} đồng")
