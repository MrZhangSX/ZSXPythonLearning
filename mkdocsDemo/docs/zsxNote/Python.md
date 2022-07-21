## 输入

**input（）函数**

````python
str = input("请输入: ");
print("你输入的内容为：" ,str)

#input 默认为字符串
print(str*2)
````

![image-20220427202815857](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220427202815857.png)

对于多行输入，只需要调用多个input并且赋值，然后回车

````python
name = input("请输入名字：")
age = input("请输入年龄： ")

print("名字：", name);
print("年龄： ", age);
````

![image-20220427203501873](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220427203501873.png)

转化输入的字符格式

````py
#转化格式
str = int(input("请输入数字："))
#str = input("请输入数字：");
print((str)*2);
````

![image-20220427205452039](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220427205452039.png)

````python
#买苹果升级
yuanPreJin = int(input("输入多少元每斤： "))
jin = int(input("输入斤数："))
price = yuanPreJin * jin;
print("总价为： ", price)
````

![image-20220427212036469](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220427212036469.png)

python字符串格式化

````python
#python字符串格式化
print("my name is %s and my age is %d" % ('zsx', 23))

#Python format 函数
#不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"));

#设置指定位置
print("{0} {1}".format("hello", "world"));
print("{1} {0} {1}".format("hello", "world"));

#设置参数
print("my name is {name}, and my age is {age}".format(name = "zsx",age = "23"));

#通过字典进行设置
zsxinfo = {"name" : "zsx", "age" : "23"};
print("my name is {name} , and my age is {age}".format(**zsxinfo));

#通过列表索引设置参数
zsxinfoList = ['zsx', '23'];
print("my name is {0[0]}, and my age is {0[1]}".format(zsxinfoList)); #列表（0）必须填

#甚至可以传入对象
class AssignValue(object):
    def __init__(self, value) :
       self.value = value;
       
my_value = AssignValue(6)
print("vakue is : {0.value}".format(my_value));
````

![image-20220428212350269](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220428212350269.png)

python数字格式化

````python
# TEST
# 定义字符串变量为输入你的名字，然后打印我的名字为
# name = input("what's your name")
# print("my name is ", name)

#定义整数变量 num = 1, 输出：我的学号为 000001
num = 1;
print("我的学号为：{:0>6d}".format(num))

#定义小数 price = 8.5、 weight = 5，输出：苹果单价 8.5元/斤，购买了5.00斤，需要支付 42.50 元
price = 8.5
weight = 5
priceAll = price * weight
print("苹果单价 {}元/斤，购买了{:.2f}斤，需要支付 {:.2f} 元".format(price, weight, priceAll))

#定义一个小时 scale = 10.01 ，输入 数据为： 10.01%
scale = 0.1001
print("数据为： {:.2%}".format(scale));
````

转义字符

````python
# 转义字符 "\"
# \ 续行符
print("line1 \
... line2 \
... line3")

# \' \\ \" 表示各自
# \t 制表符  \n 换行
print(" \\ \n \'\t\" ")
````

![image-20220428220642678](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220428220642678.png)

