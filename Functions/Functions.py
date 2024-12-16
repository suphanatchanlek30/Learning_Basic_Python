# Functions

# แบบไม่ return
def myfunc():
    print('Hello')

# เรียกใช้
myfunc()

# แบบมี พารามิเตอร์
def myfunc(name):
    print('Hello ' + name)

myfunc('Suphanat')

# แบบตั้งพารามิเตอร์เริ่มต้น
def myfunc(name = 'default'):
    """
    comments
    """
    print("test " + name)
    
# เรียกใช้
myfunc()

# แบบ return
def myfunc(number):
    return number * 2

# ตั้งตัวแปรมเก็บค่าที่ return
x = myfunc(5)

print(x);


def Time_two(var):
    return var*2

result = Time_two(4)
print(result)

# Lambda Expression การสร้างฟังก์ชั่นโดยไม่ต้องตั้งชื่อ
# lambda input : return
lambda var:var*2


