# tuple คือ สร้างแล้วไม่สามารถเปลี่ยนค่าได้ 

# tuple - imutable ไม่สามารถเปลี่ยนค่าได้
t = (1, 2, 3)
print(t[0])

# list - mutable สามารถเปลี่ยนค่าได้
my_list = [1, 2, 3] 
print(my_list[0])
my_list[0] = 4
print(my_list)
