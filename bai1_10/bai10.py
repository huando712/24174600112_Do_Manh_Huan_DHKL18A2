# Nhập lương nhân viên
salary = float(input("Nhập lương nhân viên (triệu đồng): "))

# Khởi tạo biến thuế thu nhập và lương ròng
income_tax = 0
net_salary = 0

# Tính thuế thu nhập theo quy định
if salary > 15:
    income_tax = salary * 0.30  # 30% thuế cho lương trên 15 triệu
elif salary >= 7:
    income_tax = salary * 0.20  # 20% thuế cho lương từ 7 đến 15 triệu
else:
    income_tax = salary * 0.10  # 10% thuế cho lương dưới 7 triệu

# Tính lương ròng
net_salary = salary - income_tax

# In kết quả
print(f"Thuế thu nhập: {income_tax:.2f} triệu đồng")
print(f"Lương ròng: {net_salary:.2f} triệu đồng")
