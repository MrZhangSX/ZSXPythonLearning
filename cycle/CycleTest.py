#输出从5到0
print("54321")
print("it's a joke")
i= 5;
while i >= 0:
    print(i);
    i -= 1

#循环计算0-100的和
i = 0
sum = 0;
while i <= 100:
    sum += i ;
    i += 1
print(sum) 

#循环计算 300 - 415 的和
i = 300 
sum = 0
while i <= 415:
    sum += i
    i += 1;
print(sum)

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

# 输出指定行数的星号
number = int(input("input the number you want draw: "))
count = 0;
while number > 0 and count < 20:
    print('*********************');
    number -= 1;
    count += 1;

#循环嵌套，循环中套用循环
a = 0;
while a < 2:
    b = 0;
    while b < 3:
        print('it is b')
        b += 1;
    print('it is a')
    a += 1;

#循环嵌套，输出*号三角形
number = int(input("input the number of line: "))
a = 1;
while a <= number:
    b = 1;
    while b <= a:
        print("*", end='');
        b += 1;
    a += 1; 
    print('')

# For 版本
#循环嵌套，输出*号三角形
number = int(input("input the number of line: "))
for a in range(1, number+1):
    for b in range(0, a):
        print("*", end='');
    print('')



#循环嵌套，输出数字三角形
number = int(input("input the number of line: "))
a = 1;
while a <= number:
    b = 1;
    while b <= a:
        print(b , end='');
        b += 1;
    a += 1; 
    print('')

#循环遍历计算输入字符串的字符数
inputString = input("input a string: ")
count = 0;
for char in inputString:
    count += 1;
print("conut chars are " ,count)

#计算偶数累加和
sum = 0;
a = int(input("input first range： "));
b = int(input("input end range: "));
if(a % 2 != 0):
    a += 1
for n in range(a, b, 2):
    sum += n;
print(sum)