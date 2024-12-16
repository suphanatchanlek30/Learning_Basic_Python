# Comparison and Logical Operators คือ การเปรียบเทียบทางคณิตศาสตร์

x = 1 > 2
print(x) # output = False

x = 1 >= 2
print(x) # output = False

x = 1 < 2
print(x) # output = True

x = 1 <= 2
print(x) # output = True

x = 1 == 2
print(x) # output = False

x = 1 != 2
print(x) # output = True

# เปรียบเทียบตัวอักษร
x = 'a' == 'b'
print(x) # output = False

# logic operators

y = (1 == 2) and (1 != 2)
print(y) # output = False

y = (1 == 2) or (1 != 2)
print(y) # output = True

y = not (1 == 2)
print(y) # output = True

# การใช้ not ในการเปรียบเทียบ
x = not (1 == 2)
print(x)