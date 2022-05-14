from pickletools import read_int4


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

#range()函数
for i in range(5):
    print(i)
    
#指定区间
for i in  range(0, 5):
    print(i)
    
#指定增量
for i in range(0, 10, 3):
    print(i)
    
#结合与len()函数：
for i in range(len(sites)):
    print(i, sites[i])
    
#创建列表
print(list(range(4)))

