#Lambda có riêng chỉ ở Python
def tinh_tong(a,b,c):
    return a + b + c

tong = lambda a, b, c: a + b + c
tong(1,2,3)

tinh_tong(1,2,3)


def tra_ve_gia_tri(a:tuple):
    return a[1]


lst_tuple = [(1,2),(1,3),(2,2),(3,5),(1,4)]
sorted(lst_tuple, key=lambda x: tra_ve_gia_tri(x))
lst_new = map(lambda x: x[1] + 5, lst_tuple)