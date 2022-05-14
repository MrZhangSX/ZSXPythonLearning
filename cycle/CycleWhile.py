#第一个while循环
a = 0
while a < 10:
    print(a);
    print("hello world")
    a += 2 
    
#死循环
# while True:
#     print("infinite loop");
    
'''
- break：退出该层循环
- continue：推出这次循环，并执行该层的下一次循环
'''
#break
i = 0
while i < 10 :
    print(i)
    if(i == 5):
        break
    i += 1;
    
print("break ", i )

