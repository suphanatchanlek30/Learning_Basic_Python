# For loop

seq = [1, 2, 3, 4, 5]

# for ชื่อตัวแปรอะไรก็ได้ in ชื่อของ array
for item in seq:
    print(item)
    
for i in range(0, 5):
    # จาก 0 - 4
    print(i)
    
# while loop
i = 0
while i < 5:
    print(i)
    i+=1
    # i = i + 1
    
j = 1
while j <= 5:
    print('j is currently {}'.format(j))
    j+=1