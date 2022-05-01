from cgi import print_exception
from tkinter import PROJECTING
from turtle import st


# str = input("请输入: ");
# print("你输入的内容为：" ,str)

#input 默认为字符串
#print(str*2)

#多重输入

name = input("请输入名字：")
age = input("请输入年龄： ")

print("名字：", name);
print("年龄： ", age);

#转化格式
str = int(input("请输入数字："))
#str = input("请输入数字：");
print((str)*2);

#买苹果升级

yuanPreJin = int(input("输入多少元每斤： "))
jin = int(input("输入斤数："))
price = yuanPreJin * jin;
print("总价为： ", price)

#python字符串格式化
# print("my name is %s and my age is %d" % ('zsx', 23))

#Python format 函数，基本语法是通过 {} 和 : 来代替以前的 % 。
#format 函数可以接受不限个参数，位置可以不按顺序。

#不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"));

# #设置指定位置
print("{0} {1}".format("hello", "world"));
print("{1} {0} {1}".format("hello", "world"));

# #设置参数
print("my name is {name}, and my age is {age}".format(name = "zsx",age = "23"));

# #通过字典进行设置
zsxinfo = {"name" : "zsx", "age" : "23"};
print("my name is {name} , and my age is {age}".format(**zsxinfo));

# #通过列表索引设置参数
zsxinfoList = ['zsx', '23'];
print("my name is {0[0]}, and my age is {0[1]}".format(zsxinfoList)); #列表（0）必须填

# #甚至可以传入对象
class AssignValue(object):
    def __init__(self, value) :
       self.value = value;
       
my_value = AssignValue(6)
print("vakue is : {0.value}".format(my_value));

# TEST
# 定义字符串变量为输入你的名字，然后打印我的名字为
name = input("what's your name")
print("my name is ", name)

#定义整数变量 num = 1, 输出：我的学号为 000001
num = 1;
print("我的学号为：{:0>6d}".format(num))

# #定义小数 price = 8.5、 weight = 5，输出：苹果单价 8.5元/斤，购买了5.00斤，需要支付 42.50 元
price = 8.5
weight = 5
priceAll = price * weight
print("苹果单价 {}元/斤，购买了{:.2f}斤，需要支付 {:.2f} 元".format(price, weight, priceAll))

# #定义一个小时 scale = 10.01 ，输入 数据为： 10.01%
scale = 0.1001
print("数据为： {:.2%}".format(scale));

# 转义字符 "\"
# \ 续行符
print("line1 \
... line2 \
... line3")

# \' \\ \" 表示各自
# \t 制表符  \n 换行
print(" \\ \n \'\t\" ")

