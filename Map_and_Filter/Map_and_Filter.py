# Map and filter 

seq = [1, 2, 3, 4, 5]
# Map
def time_two(var):
    return var*2

# เรียกใช้ function กับ ตัวแปรที่่เรากำหนด
print(list(map(time_two, seq)))

# Lambda Expression ลดรูป function
print(list(map(lambda var:var*2, seq)))


# Filter
# ฟังก์ชั่น ปกติ
def is_even(num):
    return num % 2 == 0

# เรียกใช้ฟังก์ชั่น, ส่ง input
print(list(filter(is_even, seq)))

# Lambda 
print(list(filter(lambda num:num % 2 == 0, seq)))