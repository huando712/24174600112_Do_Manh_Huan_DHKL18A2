# # def f(a: int = 1, b: int = 1) -> float:
# #     print(a, b)
# #     return(3.5)

# # f(1,2)
# # print()


# # def foo(bar=0, baz=1):
# #     """Thực hiện in ra 2 giá trị ra màn hình.\n
# #        Từ khóa tham số sử dụng: \n
# #        bar -- giá trị thứ nhất (default=0)\n
# #        baz -- giá trị thứ 2 (default=1)\n
# #     """
# #     print(f"bar: {bar}")
# #     print(f"baz: {baz}")

# # foo(0,1)

# # def f(a, b = 1, *args, **kwargs):
# #     print(F'a = {a}')
# #     print(F'b = {b}')
# #     print(F'args = {args}')
# #     print(F'kwargs = {kwargs}')
    
# # f(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)    

# # def f(**kwargs):
# #     print(kwargs)
# #     print(type(kwargs))
# #     for key, val in kwargs.items():
# #         print(key, '->', val)

# # f(foo=1, bar=2, baz=3)

# # # {'foo': 1, 'bar': 2, 'baz': 3}
# # # <class 'dict'>
# # # foo -> 1
# # # bar -> 2
# # # baz -> 3


# # def f(*args):
# #     print(args)
# #     print(type(args), len(args))
# #     for x in args:
# #         print(x)

# # f(1, 2, 3)

# # # (1, 2, 3)        
# # # <class 'tuple'> 3
# # # 1
# # # 2
# # # 3


# # sum(1,2)
# # sum(1,2,3)
# # sum(1,2,3,4)
# # sum(1,2,3,4,5)
# # sum(1,2,3,4,5,6)

# # # def f():
# # #     str_1 = 'foo'
# # #     return str_1

# # # s = f()
# # # print(s) #'foo'



# # # def f():
# # #     if error_cond1:
# # #         return
# # #     if error_cond2:
# # #         return
# # #     if error_cond3:
# # #         return

# # #     <normal processing>

# # # def f(x):
# # #     if x < 0:
# # #         return
# # #     if x > 100:
# # #         return
# # #     print(x)

# # # f(-3) 
# # # f(105) 
# # # f(64) #64



# # # def f():
# # #     print('foo')
# # #     print('bar')
# # #     return

# # # f()

# # # def f(qty=6, item='bananas', price=1.74):
# # #     print(f'{qty} {item} cost ${price:.2f}')

# # # f(4, 'apples', 2.24)
# # # f(4, 'apples')
# # # f(4)
# # # f()
# # # f(item='kumquats', qty=9)
# # # f(price=2.29)


# # # def f(qty, item, price):
# # #     print(f'{qty} {item} cost ${price:.2f}')

# # # f(6, item='bananas', 1.74) 
# # # #SyntaxError: positional argument follows keyword argument


# # # f(6, 'bananas', 1.74)
# # # f(qty=6, item='bananas', price=1.74)
# # # f(item='bananas', price=1.74, qty=6)
# # # f(6, price=1.74, item='bananas')
# # # f(6, 'bananas', price=1.74)



# # # def f():
# # #     s = '-- Inside f()'
# # #     print(s)

# # # print('Before calling f()')
# # # f()
# # # print('After calling f()')



# # # def f(qty, item, price):
# # #     print(f'{qty} {item} cost ${price:.2f}')

# # # f(6, 'bananas', 1.74) #truyền đúng vị trí
# # # f('bananas',6 , 1.74) #truyền sai vị trí
# # # # f(6, 1.74, 'bananas') #truyền sai vị trí
# # # # f(6, 'bananas')       #truyền thiếu
# # # f(6, 'bananas', 1.74, "$") #truyền thừa


# # #Kiểm tra điều kiện số nguyên tố
# # def kiem_tra_so_nguyen_to(x):
# #     if x < 2:
# #         return False
    
# #     for i in range(2, x):
# #         if x % i == 0:
# #             return False
# #     else:
# #         return True


# # n = int(input("Nhap vao so nguyen bat ki: "))
# # if kiem_tra_so_nguyen_to(n):
# #     print("Day la so nguyen to")
# # else:
# #     print("Day khong la so nguyen to")
    

# # def tinh_trung_binh(*args):
# #     #kiem tra gia tri trong args
# #     tong = 0
# #     for i in args:
# #         tong = tong + i
# #     trung_binh = tong/len(args)
# #     return trung_binh

# # tinh_trung_binh(1,2,3,4,5,6,7,7,8,9,10)
    


# # list_ttsv = []
# # def nhap_thong_tin_sv(**kwargs):
# #     #kiem tra cac gia tri trong kwargs
# #     if kwargs["diem_tb"] >=7:
# #         kwargs["lop"] = "A1"
# #     elif kwargs["diem_tb"] >= 4:
# #         kwargs["lop"] = "A2"
# #     else:
# #         kwargs["lop"] = "A3"
# #     list_ttsv.append(kwargs)

# # nhap_thong_tin_sv(ten="Trung", tuoi="18", diem_tb="5.0")





# # def tinh_tong_hai_so(a: int = 1, b: int = 2) -> float:
# """
#     Hàm tính toán nhận vào hai số a và b \n
#     Trả về tổng hai số này
#     """
#       return a + b

#tinh_tong_hai_so(4,5)


# print("avc","ád",12,"ádasd",4,3,2,3,5)