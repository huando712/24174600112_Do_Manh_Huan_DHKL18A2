#bài 5
char = input("Nhập một ký tự: ")
# Kiểm tra xem ký tự có phải là một ký tự hợp lệ không
if len(char) != 1 or not char.isalpha():
    print("Vui lòng nhập đúng một ký tự trong bảng chữ cái tiếng Anh.")
else:
    # Chuyển ký tự thành chữ thường để dễ kiểm tra
    char = char.lower()
    
    # Kiểm tra xem ký tự là nguyên âm hay phụ âm
    if char in 'aeiou':
        print(f"Ký tự '{char}' là nguyên âm.")
    else:
        print(f"Ký tự '{char}' là phụ âm.")