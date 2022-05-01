'''
成员运算符：
in 表示在指定序列中能否找到输入的值
not in 与in相反
'''
a = 10;
list = [1, 2, 3, 4];

if(a in list):
    print("a is in list")
else:
    print("a is not in list")
    
print("change a to 2");
a = 2;
if(a in list):
    print("a is in list")
else:
    print("a is not in list")