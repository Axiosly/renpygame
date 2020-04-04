# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 开场LOGO
image pure_black = "#000"
image pure_white =  "#ffffff"

label splashscreen:

    scene pure_black
    show pure_white with Dissolve(1.0)
    #$ renpy.pause(1, hard=True)
    show logo at truecenter with Dissolve(1.0)
    $ renpy.pause(1, hard=True)
    pause 1.0
    hide logo with Dissolve(2.0)
    $ renpy.movie_cutscene("opening.webm")
    play music "audio/因为我们在一起.mp3"
    call screen press_to_start with Dissolve(0.5)


# 主菜单之前

label opening:

    #$ renpy.movie_cutscene("opening.webm")
    return




label start:

# 游戏在此开始。
#define a = Character('夏琑（我）', color="#c8ffc8",image="Eileen")

image bg1 ="images/s1/bedroom.jpg"
# 引用游戏OP视频，在进入程序主菜单显示前自动播放。
# 此处也可以使用图片代替。
# label splashscreen:
    # $ renpy.movie_cutscene('data/op.avi')
    # return

# 游戏从这里开始。
image bg ="images/gallery/back.jpg"
show bg
with Dissolve(0.5)
define a = Character("[name]", color="#c8ffc8",image="Xs")
define b = Character("地图:", color="#11EEEE",image="Eileen")
define l = Character("蓝苑", color="#5EA294",image="Ly")
image ly sk = "s1/sk.png"
image xs ly = "s1/ly.png"
image xs ry = "s1/ry.png"

python:
    name = renpy.input("你的名字是？")
    name = name.strip()

    if not name:
         name = "夏琑"

a "我叫[name]!"
hide bg
with Dissolve(1.0)
# 下面的参数用于设定是否允许用户通过点击或快进功能跳过转场特效。
# $ _skipping = True
label s:
# 是否允许用户通过点击或快进跳过暂停时间。
# 暂停时间是通过pause命令实现的，具体请参阅官方文档。
# $ _dismiss_pause = True

# 译注：以上两个命令都是出现后生效，并且有跨label继承性，
# 通常我们设置为True以保证用户能够使用快进，
# 但如果您在特殊情况下设置为False后，应在合适的地方重新
# 调整为True，以便用户能够正常进行游戏。
# 此功能包含在最新的每夜版SDK中，当您发现正式版SDK不兼容此命令时，
# 请将SDK的更新通道设置为每夜版，并进行更新。
    show bg1
    with Dissolve(1.0)
    a "新的一天开始了。"
    show xs ry
    with Dissolve(1.0)
    "我揉了揉惺忪的眼睛，伸了个懒腰。"
    hide xs ry
    show xs ly
    with Dissolve(1.0)
    "（这时，手机屏幕亮了起来）"
    hide xs ly
    with Dissolve(1.0)
    window hide

    ##显示手机信息##
    ##重置信息列表
    $ msg_reset()
    ##输出一空行
    #$ msg_add('SP')

    #显示一条或多条信息
    #四个参数：位置|名称/标题|头像|内容
    #位置：L=左,R=右,C=中,SP=空行
    hide screen msg_dialogue
    $ m =1
    if m > 0:
        style choice_vbox:
            xalign 0.5
            ypos 600
            yanchor 0.5
            spacing gui.choice_spacing
    elif m = 0:
        style choice_vbox:
            xalign 0.5
            ypos 470
            yanchor 0.5
            spacing gui.choice_spacing
    $ msg_add('L|蓝苑|images/fnm2.png|狗子，起床了没{image=exp_f1}')
    show screen msg_dialogue
    pause
menu:
    "别一天到晚没大没小的，要叫哥哥知道不":
        jump msg2a

    "大清早的谁嘴这么臭呢，起了起了":
        jump msg2b

label msg2a:
    hide screen msg_dialogue
    $ msg_add('C|周一 7:00') #这条基中显示tips/日期信息
    $ msg_add('R|[name]|images/fnm1.png|别一天到晚没大没小的，要叫哥哥知道不{image=exp_f3}')
    show screen msg_dialogue
    pause
    jump msg3

label msg2b:
    hide screen msg_dialogue
    $ msg_add('C|周一 7:00') #这条基中显示tips/日期信息
    $ msg_add('R|[name]|images/fnm1.png|大清早的谁嘴这么臭呢，起了起了')
    show screen msg_dialogue
    pause
    jump msg3

label msg3:

    hide screen msg_dialogue
    $ msg_add('L|蓝苑|images/fnm2.png|好了好了，我就是提醒你一下，今天UIA的各国成员都要参与线上会议')
    show screen msg_dialogue
    pause

    hide screen msg_dialogue
    $ msg_add('L|蓝苑|images/fnm2.png|就你这性子我会不知道？没人催着你，没准就不去了，以往这种情况还少吗~~{image=exp_f1}')
    show screen msg_dialogue
    pause

menu:
    "喂，好歹我军衔还比你高，说话给点面子行不行":
        jump msg4a

    "大哥我错了，这次不敢了":
        jump msg4b
label msg4a:
    hide screen msg_dialogue
    $ msg_add('R|[name]|images/fnm1.png|喂，好歹我军衔还比你高，给我留点面子啊{image=exp_f4}')
    show screen msg_dialogue
    pause
    jump msg5a

label msg4b:
    hide screen msg_dialogue
    $ msg_add('R|[name]|images/fnm1.png|大哥我错了，这次不敢了{image=exp_f2}')
    show screen msg_dialogue
    pause
    jump msg5b

label msg5a:
    hide screen msg_dialogue
    $ msg_add('L|蓝苑|images/fnm2.png|是是是，您老人家才高八斗，黑客水平一流，是咱们国际情报局的中流砥柱，就算次次旷会迟到也无人敢说您')
    show screen msg_dialogue
    pause
    jump msg6a

label msg5b:
    hide screen msg_dialogue
    $ msg_add('L|蓝苑|images/fnm2.png|行了行了，一会儿见啊')
    show screen msg_dialogue
    pause
    jump msg6b

label msg6a:
menu:
    "你够了啊":
        jump msg7a

    "害，哥那么爱你哪敢不听你的话啊~":
        jump msg7b

label msg6b:
menu:
    "关闭手机屏幕":
        jump msg10

    "一会儿见~":
        jump msg7c
label msg7a:
    hide screen msg_dialogue
    $ msg_add('R|[name]|images/fnm1.png|你够了啊')
    show screen msg_dialogue
    pause
    jump msg9

label msg7b:
    hide screen msg_dialogue
    $ msg_add('R|[name]|images/fnm2.png|害，哥那么爱你哪敢不听你的话啊~')
    show screen msg_dialogue
    pause
    jump msg8

label msg7c:
    hide screen msg_dialogue
    $ msg_add('R|[name]|images/fnm2.png|一会儿见~')
    show screen msg_dialogue
    pause
    jump msg10

label msg8:
    hide screen msg_dialogue
    $ msg_add('L|蓝苑|images/fnm2.png|MMP{image=exp_f4}快别恶心我了')
    show screen msg_dialogue
    pause

label msg9:
    hide screen msg_dialogue
    $ msg_add('L|蓝苑|images/fnm2.png|行了行了，等会儿赶紧的哈')
    show screen msg_dialogue
    pause
    jump msg6b

label msg10:
    hide screen msg_dialogue
    ##关闭手机信息##
    window show
a "该走喽"
scene lab
with fade
label lab1:
b "UIA情报局实验室"
jump lab2
