import csv
def doc_file(list_cauthu: list):
    with open(file="file\\ds_cauthu.csv", mode ="r") as open_file:
     csv_reader = csv.reader(open_file)
     for item in csv_reader:
        print(item)
        list_cauthu.append(item)

def nhap_thong_tin(list_cauthu):
 while True:
    try:
      ma_cau_thu= input("nhap vao ma cau thu")
      ten_cau_thu= input("ten cau thu")
      ten_doi_bong= input("ten doi bong")
      tuoi= int(input("nhap vao tuoi"))
      vi_tri=input("nhap vao vi tri")
      assert vi_tri=="thu mon" or vi_tri=="hau ve" or vi_tri=="tien ve" or vi_tri=="tien dao"
      so_ban_thang = int(input("nhap vao so ban thang"))
      
    except:
      print(" yeu cau nhap lai")
    else:
      if so_ban_thang >10:
        thuong= so_ban_thang*5000000
        tro_cap = 0.1
      elif so_ban_thang >= 5:
        thuong= so_ban_thang *300000
        tro_cap = 0.2
      else:
        thuong = so_ban_thang *200000
        tro_cap = 0.3
        if vi_tri == "thu mon":
          luong = 500000+500000*tro_cap+thuong
        elif vi_tri == "hau_ve":
          luong = 700000+700000*tro_cap+thuong
        elif vi_tri == "tien ve":
          luong= 900000+900000*tro_cap+thuong
        elif vi_tri == "tien dao":
          luong = 1000000+1000000*tro_cap+thuong
          list_cauthu.append([ma_cau_thu, ten_cau_thu, ten_doi_bong, tuoi, vi_tri, so_ban_thang, luong, tro_cap])
          break
def sua_thong_tin(list_cauthu: list):
  ma_ct = input()
  count = 0
  vi_tri_sua = -1
  for i in range(len(list_cauthu)):
    if list_cauthu[i][0] == ma_ct:
      count += 1
      vi_tri_sua = 1
      break
    if count !=0:
     print("co cau thu nay trong ds")
     while True:
       try:
         ma_cau_thu=input()
         ten_cau_thu = input()
         ten_doi_bong = input()
         tuoi= int(input())
         vi_tri= input
         assert vi_tri=="thu mon" or vi_tri=="hau ve" or vi_tri=="tien ve" or vi_tri=="tien dao"
         so_ban_thang = int(input())
       except:
         print(" lỗi yêu cầu nhập lại")
       else:
         if so_ban_thang >10:
             thuong= so_ban_thang*5000000
             tro_cap = 0.1
         elif so_ban_thang >= 5:
            thuong= so_ban_thang *300000
            tro_cap = 0.2
         else:
           thuong = so_ban_thang *200000
           tro_cap = 0.3
         if vi_tri == "thu mon":
          luong = 500000+500000*tro_cap+thuong
         elif vi_tri == "hau_ve":
          luong = 700000+700000*tro_cap+thuong
         elif vi_tri == "tien ve":
          luong= 900000+900000*tro_cap+thuong
         elif vi_tri == "tien dao":
          luong = 1000000+1000000*tro_cap+thuong
          cau_thu_thay_the =([ma_cau_thu, ten_cau_thu, ten_doi_bong, tuoi, vi_tri, so_ban_thang, luong, tro_cap])
          list_cauthu[vi_tri_sua]= cau_thu_thay_the
          break
         else:
           print("cau thu khong ton tai")

def luu_file(list_cauthu):
  with open(file="file\ds_cauthu.csv", mode = "w") as open_file:
    csv_writer= csv.writer(open_file)
    for item in list_cauthu:
      csv_writer.writerow(item)


            

        
