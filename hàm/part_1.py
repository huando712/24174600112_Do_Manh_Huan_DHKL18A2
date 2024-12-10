#cơ bản
# def ten_ham(tham_so_1, tham_so_2):
#     return tham_so_1*tham_so_2
# ket_qua=ten_ham(4,5)
# print(ket_qua)
    







# def f():
#     s = '-- Inside f()'
#     print(s)
# print('Before calling f()')
# f()
# print('after calling f()')


# def f(qty, item, price):
#     print(f'{qty} {item} cost ${price:.d2f}')
# f(6, 'bananas', 1.74)
def f(a, b=1, *args, **kwargs):
    
     print(F'a ={a}')
     print(F'b = {b}')
     print(F'args = {args}')
     print(F'kwargs = {kwargs}')
f(1, 2, 'foo', 'bar', 'baz', 'qux')     

