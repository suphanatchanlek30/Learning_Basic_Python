# Various Useful Methods
st = 'hello my name is Steve'

print(st.lower())
print(st.upper())
print(st.title()) #ตัวแรกของคำให้เป็นตัวใหญ่

print(st.split())
print(st.split('h'))

# dictionaries
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())
print(d.values())
print(d.items())

my_list = [1, 2, 3, 'a']
my_list.append(4);
print(my_list)
my_list.pop(0) #ลบตัวแรก index ที่ 0
print(my_list)

# ค้นหาใน list
print(1 in my_list) # false
print(2 in my_list) # true
print('a' in my_list) # true

