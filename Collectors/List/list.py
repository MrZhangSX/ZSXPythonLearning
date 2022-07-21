
list = ['red', 'green', 'blue']
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#访问列表中的值，若值为正数则为顺序读取
print(list[0]);
print(list[1]);
print(list[2]);

#使用负数索引，则为反向索引，从尾部读取
print(list[-1]);
print(list[-2]);
print(list[-3]);

#使用下标索引截取字符
print(nums[0 : 4]);
#亦可搭配负数下标进行截取
print(nums[1 : -2]);

#更新列表。直接取下标进行替换，也可以使用append()方法进行添加项
print("更新前：" , list[1]);
list[1] = 'white';
print("更新后： " , list[1]);

list.append('yello');
print(list);

#使用del和remove()语句删除
del list[2];
print(list)

'''
列表脚本操作符
len(list) 返回列表长度
+ 列表组合
* 别表重复
object in list object是否存在在列表里
for x in [1, 2, 3]: 列表循环
'''