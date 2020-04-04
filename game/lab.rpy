

label lab2:
    define c = Character('蓝苑', kind=nvl, color="#5EA294")
    define d = Character('指挥长', kind=nvl, color="#c8c8ff")
    define e = Character('情报科', kind=nvl, color="#99668F")
    define f = Character('同事A', kind=nvl, color="#5577AA")
    define g = Character('[name]', kind=nvl, color="#4D9EB3")
    "线上会议中..."
    d "本次临时召开线上会议主要是有一件重大的事情需要引起重视。"
    d "那么,接下来先请我们情报科的同事来简单汇报一下。"
    e "咳咳"
    e "情况是这样的,我们接到组里潜伏在黑手党的线人可靠消息,黑手党为了满足自己的野心正谋划着窃取各国的军情机密,企图控制所有国家。"
    f "不会吧,他们做什么春秋大梦呢,说的倒轻巧,这几千年来有人成功了么?"
    d "话虽如此,但只怕这又将掀起一场腥风血雨.你们可还记得我们UIA的职责是什么?"
    nvl clear
    e "是的,我们成立的初心便是作为维系各国各组织关系平衡,维护世界和平,既然不是空穴来风,那我们就不能掉以轻心。"
    d "没错,首先必须先确保我们UIA资料库的安全性,这点相信有[name]在不用太过担心,然后我们要密切关注各国高层之间的动向,防止黑手党的人伺机行动。"
    d "[name],这件事情我想交由你和蓝苑负责可以吗?"
    g "收到。"
    d "蓝苑呢,有什么问题吗?"
    d "蓝苑!"
    nvl clear
    c "啊,在在。"
    c "好的指挥长。"
    d "那么接下来.....(此处省略几百字)......行吧,有什么问题大家随时汇报,散会。"
    nvl clear

label lab3:
    show screen ccc
    hide screen ccc
    scene 1-2_cg
label lab4:
    show lab
    "从开会开始,蓝苑似乎就看起来有些心不在焉。"
    show ly sk
    with Dissolve(1.0)
    l "我到底......能掌握住自己的命运么"
    a "蓝苑,你发什么呆啊?"
    hide ly sk
    return
