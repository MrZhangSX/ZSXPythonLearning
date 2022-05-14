## 循环



### while

````python
#一般格式
while  判断条件(condition):
    执行语句(statements)..
#例子：
#第一个while循环
a = 1
while a < 10:
    print(a);
    a += 2 
````

**计算机执行的三种流程**

- 顺序：从上至下，顺序执行代码
- 分支：根据条件判断，决定运行的分支
- 循环：让特定代码执行数次

PS：如果要设置数字循环条件，尽量从0开始， 因为我们数组以及集合的第一个元素的下标为0

#### 死循环：即不能终结循环，循环部分一直运行

````python
#死循环
while True:
  print("infinite loop");
#最常见最是 while True，或者给一个一定为True的条件,需要与break配合
````



### break 和 continue

- **break：退出该层循环**
- **continue：推出这次循环，并执行该层的下一次循环**

````python
#break
i = 0
while i < 10 :
    print(i)
    if(i == 5):
        break
    i += 1;
    
print("break ", i )

#continue break 结合
#输入exit退出
flag = True
while flag:
    str = input("input a string: ")
    if(str == "zsx"):
        print("wow, you are zsx")
        continue
    if(str == "exit"):
        flag = False;
    print("you input: ", str);
    
print("exit")
````



### For

````python
#一般格式
for <variable> in <sequence>:
    <statements>
else:
    <statements>
#一般用于遍历数组等变量
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
````



#### while 和 for

- while 主要设置循环终结条件来控制循环，而For 主要用来遍历数据

