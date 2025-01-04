#câu a.  S = 1 + 2 + 3 + 4 + ⋯ + n
while True:
    try:
        n=int(input("nhap vao so nguyen duong"))
        if n >0  :
            
            break
        else:
            print("nhạp sai vui lòng nhập lại")
    except:
        print("nhap sai")
s=0
for i in range(1, n+1):
    s=s+i
    print(f"ket qua cau a :{s} ")



#câu b   𝑆 = 1+1/2+1/3+1/4......+1/n
while True:
    try:
        n = int(input("nhap vao so nguyen duong:"))
        if n >0:
            break
        else:
            print("vui long nhap vao so lon hon 0")
            
    except:
        print("yeu cau nhap lai")
tong=0 
for i in range(1, n+1):
    tong+= 1/i
print(f"ket qua  cau b :  {tong:.2f}")


#cau c s=1+1/2-1/3+1/4-.....+1/n+1-1/n
while True:
    try:
        n = int(input("nhap vao so nguyen duong:"))
        if n >1: #vì có 2 sô hạng n lên phải lớn hơn 11
            break
        else:
            print("vui long nhap vao so nguyen duong")
    except:
        print("nhap sai")
tong = 1

for i in range(2, n+1):
    if i%2==0:
        tong+=1/i #nếu chia hết cho 2 thì cộng
    else:
        tong-=1/i
    
print(f"ket qua cau c:{tong:.2f}")

#câu d: 1+1/1*2+1/1*3+1/1*4+.....+1/(n-1)*n
while True:
    try:
        n = int(input("nhap vao so nguyen duong:"))
        if n>1:
            break
        else:
            print("nhap sai vui long nhap so lon hon 0")
    except:
        print("nhap sai")
tong = 0
for i in range(1, n):  # Lặp từ i = 1 đến i = n-1
    tong += 1 / (i * (i + 1))  # Cộng dồn giá trị của 1 / (i * (i + 1)) vào S
print(f"ket qua cau d: {tong:.2f}")

#cau f s=1+2+3+4+5...+n/n+1
while True:
    try:
        n= int(input("nhap vao so nguyen duong :"))
        if n>0:
            break
        else:
            print(" vui long nhap lai")
    except:
        print("error")
tong = 0       
for i in range (1, n+1):
    tong+=i
s=tong/1+n
print(f"tong {s}") 

            

            

