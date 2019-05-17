bingo = '复读机'
answer = input('人类的本质是什么：')
while True:
    if answer == bingo:
        break
    answer = input('人类的本质是什么（说对才能结束游戏）：')
print('没错，就是复读机')
