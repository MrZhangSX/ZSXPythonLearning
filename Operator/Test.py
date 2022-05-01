# '''
# 1.判断除数是否为0
#   输入num1和num2  如果num2不为0，计算num1除以num2
# '''
# num1 = int(input("输入num1： "));
# num2 = int(input("输入num2: "));
# if(num2 != 0):
#     print("计算结果为： ", num1 / num2);
# else:
#     print("除数num2 为 0");

# #计算器

# num1 = int(input("输入num1： "));
# num2 = int(input("输入num2: "));
# operator = input("输入要进行的操作: ")
# if(operator == '+'):
#     print("num1 + num2 = ", num1 + num2)
# elif(operator == '-'):
#     print("num1 - num2 = ", num1 - num2)
# elif(operator == '*'):
#     print("num1 * num2 = ", num1 * num2)
# elif(operator == '/'):
#     print("num1 / num2 = {}".format(num1 / num2))
# else:
#     print("input error")

# # 判断偶数
# num1 = int(input("输入num1: "));
# if(num1 % 2 == 0):
#     print("num1是偶数")
# else:
#     print("num1是奇数")

# # 判断正负
# num1 = int(input("输入num1："))
# if(num1 > 0):
#     print("num1 是正数")
# elif(num1 < 0):
#     print("num1 是负数")
# else:
#     print("num1 为 0")

# # 通过input输入一个输，编写代码判断该数是否在0到120之间
# num1 = int(input("input num1: "));
# if(num1 >= 0 and num1 <= 120):
#     print("0<= num1 <= 120")
# else:
#     print("num1<0 or num1 > 120")
    
# # 输入username和password，只有username = zsx，密码为 zsxxsz 才通过
# username = input("input your username: ");
# password = input("input your password : ");

# #方法一 逻辑运算符
# if(username == "zsx" and password == "zsxxsz"):
#     print("log in success")
# else:
#     print("username or password is wrong")

# #方法二 if多重判断
# if(username == "zsx"):
#     if(password == "zsxxsz"):
#         print("log in successfully")
#     else:
#         print("password is wrong, please check")
# else:
#     print("username is wrong, please check")

# #输入age，如果age<10，小孩，<20 小朋友，小于30 年轻人， 小于50 中年人， 其余为老人
# age = int(input("input your age: "))
# if(age < 0):
#     print("please check your input")
# elif(age < 10):
#     print("小孩")
# elif(age < 20):
#     print("小朋友")
# elif(age < 30):
#     print("年轻人")
# elif(age < 50):
#     print("中年人")
# else:
#     print("老年人")

# 输入name 如果为tom 接着输入age
name = input("input name: ")
if(name == "tom"):
    age = int(input("input your age: "))
    if(age >= 30):
        print("大叔")
    else:
        print("小弟")
else:
    print("姓名错误")