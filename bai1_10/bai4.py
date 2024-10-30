#bài 4
#nhập cạnh của tam giác
a = float(input("nhập cạnh a:"))
b = float(input("nhập cạnh b:"))
c = float(input("nhập cạnh c:"))
if a+b>c and a+c>b and c+b>a:
    if a==b==c:
        print("tam giác đều")
    elif a==b or b==c or a==c:
        print("tam giác cân")
        if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (b**2+c**2==a**2):
            print("tam giác vuông")
        elif a==b or b==c or a==c and (a**2+b**2==c**2) or (a**2+c**2==b**2) or (b**2+c**2==a**2):
            print("tam giác vuông cân")
        else:
            print("tam giác thường")
else:
    print("không phải bộ ba cạnh của tam giác")        