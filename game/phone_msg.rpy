# 您可以在此编写游戏的脚本。
#PhoneMsg 手机信息显示窗口
screen msg_dialogue():
    tag msg_t
    zorder 0

    $ count = 1
    vbox:
        xfill True
        ##创建一个frame
        frame:
            #xsize 1000 #宽
            xfill True
            ysize 450 #高
            xalign 0.5 #水平基中
            ypos 35 #距离顶部
            padding(100,0,100,0)
            #background "#ffde00"
            background  None

            viewport:
                yinitial 1.0
                vbox:
                    use msg_show
#显示手机单条信息
screen msg_show():
    for d in msg_list:
        $ temp_msg_list = d.split('|')
        $ temp_msg_len  = len(temp_msg_list)
        $ msg_place = temp_msg_list[0] #标志L左,R右,C中间,SP空行
        if temp_msg_len > 1:
            $ msg_name = temp_msg_list[1] #名字，C=标题
            if temp_msg_len > 2:
                $ msg_face = temp_msg_list[2] #头像
                $ msg_txt = temp_msg_list[3] #内容
            else:
                $ msg_face = '' #头像
                $ msg_txt = '' #内容
        else:
            $ msg_name = '' #名字，C=标题
            $ msg_face = '' #头像
            $ msg_txt = '' #内容


        frame:
            xfill True
            #background "#4EA1E0"
            background  None

            if msg_place == 'SP':
                vbox:
                    #text 'SP'
                    null height 50 #空格一行

            if msg_place == 'C':
                frame:
                    background  Frame("images/msg_c_bg.png", 4, 4, 4, 4)
                    padding(5,2,5,2)
                    xalign 0.5
                    vbox:
                        text msg_name:
                            text_align 0.5
                            size 16
                            color '#ffffff'

            if msg_place == 'R':
                hbox:
                    xalign 1.0
                    ##右边信息
                    frame:
                        background  None
                        vbox:
                            frame:
                                xalign 1.0
                                background  None
                                padding(5,0,10,5)
                                vbox:
                                    text msg_name:
                                        size 18
                                        text_align 1.0
                                        color '#cccccc'
                                        font "Font.ttf"
                            frame:
                                background  Frame("images/msg_right_bg.png", 4, 20, 9, 4)
                                padding(15,10,15,10)
                                xmaximum 500 #水平最大宽度
                                vbox:
                                    text msg_txt:
                                        text_align 1.0
                                        color '#232323'
                                        font "SourceHanSans-Light-Lite.ttf"
                    frame:
                        background  None
                        xsize 105
                        ysize 105
                        xalign 1.0
                        add im.Scale("images/fnm1.png", 80, 80) xalign 0.5 yalign 0.0

            if msg_place == 'L':
                ##左边信息
                hbox:
                    frame:
                        background  None
                        xsize 105
                        ysize 105
                        add im.Scale("images/fnm2.png", 80, 80) xalign 0.5 yalign 0.0
                    frame:
                        background  None
                        vbox:
                            frame:
                                background  None
                                padding(10,0,5,5)
                                vbox:
                                    text msg_name:
                                        size 18
                                        color '#cccccc'
                                        font "Font.ttf"
                            frame:
                                background  Frame("images/msg_left_bg.png", 9, 20, 4, 4)
                                padding(15,10,15,10)
                                xmaximum 500 #水平最大宽度
                                vbox:
                                    text msg_txt:
                                        text_align 0.0
                                        color '#232323'
                                        font "SourceHanSans-Light-Lite.ttf"




#全局变量，存放信息列表
default  msg_list = []
image exp_f1 = "images/exp/f1.png"
image exp_f2 = "images/exp/f2.png"
image exp_f3 = "images/exp/f3.png"
image exp_f4 = "images/exp/f4.png"
image exp_f5 = "images/exp/f5.png"

init python:

    #重置/清空列表信息函数
    def msg_reset():
        global msg_list
        msg_list=[]

    #添加一条手机信息
    def msg_add(str):
        global msg_list
        msg_list.append(str)
