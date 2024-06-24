# 版权所有702361946@qq.com
# @2024
# python 3.12
# PyCharm Community Edition 2024.1.1
import os
from tkinter import *
from tkinter import messagebox

temp = ''

with open('zh_question.txt', 'r', encoding='UTF-8') as question:
    for txt in question.readlines():
        question = txt.split(';')

with open('zh_evaluate.txt', 'r', encoding='UTF-8') as evaluate:
    for txt in evaluate.readlines():
        evaluate = txt.split(';')

with open('user.txt', 'r+', encoding='UTF-8') as user:
    for txt in user.readlines():
        user = txt.split(';')


def win_destroy():
    win.destroy()


def esc():
    os.abort()


def def_question(txt0):
    win = Tk()
    win.title("game_if")
    win.geometry("320x180")
    win.iconbitmap("1.ico")
    win.resizable(False, False)
    messagebox0 = messagebox.askquestion('?', txt0)
    global temp
    if messagebox0 == 'yes':
        temp = 'y'
    elif messagebox0 == 'no':
        temp = 'n'
    win.destroy()
    win.mainloop()


def def_evaluate(txt0):
    txt = open('user.txt', 'w+', encoding='UTF-8')
    txt.write(txt0)
    txt.close()
    win = Tk()
    win.title("game_if")
    win.geometry("320x180")
    win.iconbitmap("1.ico")
    win.resizable(False, False)

    message0 = Message(win, text=('您或许可以当:' + txt0), width=320)
    message1 = Message(win, text='感谢游玩《听说你想做游戏》', width=320)
    button0 = Button(win, text='确定', command=esc)

    message0.pack()
    message1.pack()
    button0.pack()

    win.mainloop()


def user():
    win = Tk()
    win.title("game_if")
    win.geometry("320x180")
    win.iconbitmap("1.ico")
    win.resizable(False, False)

    message0 = Message(win, text=('您上次选择完后,您或许可以当:' + user[0]))
    button0 = Button(win, text='确定', command=win_destroy)

    message0.pack()
    button0.pack()

    win.mainloop()


# 开始页
if True:
    win = Tk()
    win.title("game_if")
    win.geometry("320x180")
    win.iconbitmap("1.ico")
    win.resizable(False, False)

    print('''欢迎游玩《听说你想做游戏》
思路源于文件夹中的图片
感谢qq877599174
877599174@qq.com
版权所有702361946@qq.com @2024''')

    message0 = Message(win, text='《听说你想做游戏》', width=320)
    button0 = Button(win, text='开始', command=win_destroy)
    button1 = Button(win, text='记录', command=user)
    button2 = Button(win, text='退出', command=esc)

    message0.pack()
    button0.pack()
    button1.pack()
    button2.pack()

    win.mainloop()

# 游戏页
if True:
    def_question(question[0])
    if temp == 'y':
        def_question(question[1])
        if temp == 'y':
            def_question(question[2])
            if temp == 'y':
                def_evaluate(evaluate[0])
            elif temp == 'n':
                def_evaluate(evaluate[1])
        elif temp == 'n':
            def_question(question[3])
            if temp == 'y':
                def_evaluate(evaluate[2])
            elif temp == 'n':
                def_question(question[4])
                if temp == 'y':
                    def_evaluate(evaluate[3])
                elif temp == 'n':
                    def_question(question[5])
                    if temp == 'y':
                        def_question(question[6])
                        if temp == 'y':
                            def_evaluate(evaluate[5])
                        elif temp == 'n':
                            def_evaluate(evaluate[6])
                    elif temp == 'n':
                        def_evaluate(evaluate[4])
    elif temp == 'n':
        def_question(question[7])
        if temp == 'y':
            def_question(question[9])
            if temp == 'y':
                def_question(question[15])
                if temp == 'y':
                    def_question(question[16])
                    if temp == 'y':
                        def_question(question[17])
                        if temp == 'y':
                            def_question(question[18])
                            if temp == 'y':
                                def_question(question[19])
                                if temp == 'y':
                                    def_evaluate(evaluate[15])
                                elif temp == 'n':
                                    def_question(question[20])
                                    if temp == 'y':
                                        def_evaluate(evaluate[16])
                                    elif temp == 'n':
                                        def_question(question[21])
                                        if temp == 'y':
                                            def_evaluate(evaluate[18])
                                        elif temp == 'n':
                                            def_evaluate(evaluate[17])
                            elif temp == 'n':
                                def_question(question[22])
                                if temp == 'y':
                                    def_evaluate(evaluate[19])
                                elif temp == 'n':
                                    def_evaluate(evaluate[20])
                        elif temp == 'n':
                            def_evaluate(evaluate[14])
                    elif temp == 'n':
                        def_question(question[23])
                        if temp == 'y':
                            def_evaluate(evaluate[21])
                        elif temp == 'n':
                            def_question(question[24])
                            if temp == 'y':
                                def_question(question[25])
                                if temp == 'y':
                                    def_question(question[26])
                                    if temp == 'y':
                                        def_question(question[27])
                                        if temp == 'y':
                                            def_evaluate(evaluate[26])
                                        elif temp == 'n':
                                            def_evaluate(evaluate[25])
                                    elif temp == 'n':
                                        def_evaluate(evaluate[24])
                                elif temp == 'n':
                                    def_evaluate(evaluate[23])
                            elif temp == 'n':
                                def_evaluate(evaluate[22])
                elif temp == 'n':
                    def_question(question[28])
                    if temp == 'y':
                        def_question(question[29])
                        if temp == 'y':
                            def_question(question[30])
                            if temp == 'y':
                                def_evaluate(evaluate[29])
                            elif temp == 'n':
                                def_evaluate(evaluate[28])
                        elif temp == 'n':
                            def_evaluate(evaluate[27])
                    elif temp == 'n':
                        def_question(question[31])
                        if temp == 'y':
                            def_question(question[34])
                            if temp == 'y':
                                def_evaluate(evaluate[33])
                            elif temp == 'n':
                                def_question(question[35])
                                if temp == 'y':
                                    def_question(question[36])
                                    if temp == 'y':
                                        def_evaluate(evaluate[35])
                                    elif temp == 'n':
                                        def_question(question[37])
                                        if temp == 'y':
                                            def_evaluate(evaluate[36])
                                        elif temp == 'n':
                                            def_evaluate(evaluate[37])
                                elif temp == 'n':
                                    def_evaluate(evaluate[34])
                        elif temp == 'n':
                            def_question(question[32])
                            if temp == 'y':
                                def_evaluate(evaluate[30])
                            elif temp == 'n':
                                def_question(question[33])
                                if temp == 'y':
                                    def_evaluate(evaluate[31])
                                elif temp == 'n':
                                    def_evaluate(evaluate[32])
            elif temp == 'n':
                def_question(question[10])
                if temp == 'y':
                    def_question(question[11])
                    if temp == 'y':
                        def_evaluate(evaluate[10])
                    elif temp == 'n':
                        def_question(question[12])
                        if temp == 'y':
                            def_evaluate(evaluate[11])
                        elif temp == 'n':
                            def_question(question[13])
                            if temp == 'y':
                                def_question(question[14])
                                if temp == 'y':
                                    def_evaluate(evaluate[13])
                                elif temp == 'n':
                                    def_evaluate(evaluate[12])
                            elif temp == 'n':
                                def_evaluate(evaluate[12])
                elif temp == 'n':
                    def_evaluate(evaluate[9])
        elif temp == 'n':
            def_question(question[8])
            if temp == 'y':
                def_evaluate(evaluate[7])
            elif temp == 'n':
                def_evaluate(evaluate[8])
