def tinh_trung_binh(*args):
    tong=0
    for i in args:
        tong +=1
        trung_binh = tong/len(args)
        return trung_binh
tinh_trung_binh(1,2,3,4,5,6,7,8,9,10)   
print(tinh_trung_binh) 




list_ttsv=[]
def nhap_thong_tin_sv(**kwargs):
    #kiểm tra các giá trị tromg kwargs
    if kwargs["diem_tb"] >=7:
        kwargs["lop"] = "a1"
    elif kwargs["diem_tb"]  >=5:
        kwargs["lop"]  = "a2"

              