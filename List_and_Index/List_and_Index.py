# list
# example list
my_list1 = [1, 2, 3, 4, 5]
print(my_list1)

my_list2 = ['hi', 0, 1, 2, 3]
print(my_list2)

# append list คือ การเพิ่มข้อมูล จะนำข้อมูลที่เพิ่ม มาต่อท้าย
my_list1.append(6)
print(my_list1)

# index list เริ่มต้นที่ 0
my_list3 = ['a', 'b', 'c', 'd', 'e']
print(my_list3[0])
print(my_list3[1])
print(my_list3[2])
print(my_list3[3])
print(my_list3[4])

# กำหนดค่าให้แต่ละ index
my_list3[0] = 'z'
print(my_list3)

# print index 0 ถึง index 2
print(my_list3[0:3]) #[start:stop+1]

nested = [1, 2, ['a', 'b']]
print(nested[2][0:2])