import easygui as g
import sys


while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏^-^')

    msg = "请问人类的本质是什么？"
    title = "小游戏互动"
    choices = ['傻吊','复读机','ooxx','沙雕']

    choice = g.choicebox(msg,title,choices)


    g.msgbox('你选择的是：' + str(choice),'结果')

    msg = '想再选一次吗？'

    title = "请选择"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit()
