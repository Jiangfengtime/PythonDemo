# easygui的三种导入方式
# 方式一：import easygui
# 方式二：from easygui import *
# 方式三：import easygui as g

import easygui as g
import sys
while True:
    # msgbox(msg, title):第一个参数是提示框内容；第二个参数是提示框标题
    g.msgbox("欢迎进入第一个游戏界面", '游戏')
    msg = "你最喜欢的水果是什么："
    title = "调查问卷"
    choices = ['香蕉', '西瓜', '苹果', '葡萄']
    # choicebox(msg, title, choices):选项box
    # 第一个参数是单选框的内容
    # 第二个参数是单选框的标题
    # 第三个参数是单选框的选项列表
    # choice = g.choicebox(msg, title, choices)

    # buttonbox(msg, title, choices):按钮box，和choicebox功能差不多
    choice = g.buttonbox(msg, title, choices)

    g.msgbox("你选择的是：" + str(choice), '结果')

    msg = '需要重新选择吗？'
    title = '请选择：'

    # ccbox(msg, title, choices):    [c:continue c:cancel]
    # ynbox(msg, title, choices):    [y:yes      n:no]
    # indexbox(msg, title, choices)  [左:0       右:1]
    # 第一个参数是选择的题目
    # 第二个参数是选择框的标题
    # 第三个参数是按钮名称
    if g.ccbox(msg, title):
        pass
    else:
        # sys.exit(0)：退出
        # sys.exit(0)

        # 输入文本框
        # g.enterbox("对本游戏有什么看法", '游戏反馈')

        # 输入整数
        # integerbox(msg, title, default, lowerbound, upperbound):
        # 第一个参数是提示框，第二个参数是标题
        # 第三个参数是默认值，第四、第五参数表示允许输入的区间范围
        # g.integerbox("给本游戏打分", '评分', 10, 1, 10)

        # 文本输入框
        # list1 = ['用户名:', '密码:', '电话号码:']
        g.multenterbox("提示内容", '标题', ['用户名'])
        g.multpasswordbox("密码", '标题', ['密码'])

        sys.exit(0)





