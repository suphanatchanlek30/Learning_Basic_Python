# Range range() เอาไว้กำหนดต่างๆ

# สร้างจำนวน 0 - 4
# ตัวที่ 0 - n-1
for i in range(0, 5):
    print(i)
    
# ตัวที่ n-1 - 0
# เริ่มจาก 5
# ลดทีละ 1
# จนเหลือ 1
for i in range(5, 0, -1):
    print(i)
    
for i in range(0, 20, 2):
    print(i)

print(list(range(0, 20, 2)))

# List comprehension ย่อ for loop มาใช้กับ list ทำให้โค้ดง่ายขึ้นและสั้น
x = [1, 2, 3, 4]
# Original for loop
out = []
for num in x:
    out.append(num**2)
    
print(out) # [1, 4, 9, 16]

# List comprehension สามารถพิมพ์ได้เลย
out = [num**2 for num in x]
print(out)

