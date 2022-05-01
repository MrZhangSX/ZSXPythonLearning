#python 中，变量是以内容为基准而不是像 c 中以变量名为基准，
#所以只要你的数字内容是5，不管你起什么名字，这个变量的 ID 是相同的
#在脚本式编程环境中没有问题。但是在交互式环境中，编译器会有一个小整数池的概念，会把（-5，256）间的数预先创建好，
#而当a和b超过这个范围的时候，两个变量就会指向不同的对象了，因此地址也会不一样
from xml.sax.handler import property_interning_dict


a = 5;
b = 5;
print(id(a));
print(id(b));
print(a is b);

a= 3000;
b = 3000;
print(id(a));
print(id(b));
print(a is b);

#is 判断两个对象是否为同一对象, 是通过 id 来判断的; 当两个基本类型数据(或元组)内容相同时, id 会相同, 但并不代表 a 会随 b 的改变而改变。
#== 判断两个对象的内容是否相同, 是通过调用 __eq__() 来判断的
#列表是相同的，但元组的标识是跟着变量名的，变量名不一样，标识也不一样。
tuple1 = (1000,2000);
tuple2 = (1000,2000);
print(id(tuple1[0]));
print(id(tuple2[0]));
if(tuple1[0] is tuple2[1]):
    print(" is the same")
else:
    print("Not the same ")
