import random

a = random.randint(10,20)
print(a)

#随机数判断进公司顺序
i = random.randint(1,7)
if(i == 1):
    print("zsx");
elif(i == 2):
    print("wgq");
elif(i == 3):
    print("ouyang")
elif(i == 4):
    print("lf")
elif(i == 5):
    print("junwu")
elif(i == 6):
    print("huangyi")
else:
    print("Roise")
    
list = ["石头","剪刀","布"];
pc = list[random.randint(0,2)]
print("输入你要出的数字：0 石头，1 剪刀， 2布")
player = list[int(input())]
if(pc == player):
    print("电脑出的为 {}， 你出的为 {}, 平局".format(pc, player));
elif((pc == "石头" and player == "剪刀") or (pc == "剪刀" and player == "布") or (pc == "布" and player == "石头")):
    print("电脑出的为 {}， 你出的为 {}，电脑胜".format(pc, player));
else:
    print("电脑出的为 {}， 你出的为 {}，你胜".format(pc, player));