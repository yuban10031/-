import random
print('_______第二个傻吊编程__________\n')
secret = random.randint(1,10)
temp = input("请猜一个数：")
guess = int(temp)
i = 0
while guess != secret and i<3:
    i = i+1
    temp = input("猜错了，请重新输入：")
    guess = int(temp)
    if guess == secret:
        print("猜对了")
    if guess > secret:
        print("大了大了")
    else:
        print("太小了")
print("游戏结束")
    
