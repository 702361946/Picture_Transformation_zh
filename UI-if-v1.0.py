# 版权所有702361946@qq.com
# @2024
# python 3.12
# PyCharm Community Edition 2024.1.1
import os
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
    pass

with open('zh_problem.txt', 'r', encoding='UTF-8') as problem:
    for txt in problem.readlines():
        problem = txt.split(';')

with open('zh_evaluate.txt', 'r', encoding='UTF-8') as evaluate:
    for txt in evaluate.readlines():
        evaluate = txt.split(';')

with open('user.txt', 'r+', encoding='UTF-8') as USER:
    for txt in USER.readlines():
        USER = txt.split(';')


def win_destroy():
    win.destroy()


def esc():
    os.abort()


def def_problem(txt0):


    win = Tk()
    win.title("game_if")
    win.geometry("320x180")
    win.iconbitmap("1.ico")
    win.resizable(False, False)
    messagebox0 = messagebox.askquestion('?', txt0)
    win.destroy()
    win.mainloop()
    if messagebox0 == 'yes':
        return True
    elif messagebox0 == 'no':
        return False



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
    def win_destroy():
        win.destroy()
    win = Tk()
    win.title("game_if")
    win.geometry("320x180")
    win.iconbitmap("1.ico")
    win.resizable(False, False)

    message0 = Message(win, text=('您上次选择完后,您或许可以当:' + USER[0]))
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
    if def_problem(problem[0]):
        if def_problem(problem[1]):
            if def_problem(problem[2]):
                def_evaluate(evaluate[0])
            else:
                def_evaluate(evaluate[1])
        else:
            if def_problem(problem[3]):
                def_evaluate(evaluate[2])
            else:
                if def_problem(problem[4]):
                    def_evaluate(evaluate[3])
                else:
                    if def_problem(problem[5]):
                        if def_problem(problem[6]):
                            def_evaluate(evaluate[5])
                        else:
                            def_evaluate(evaluate[6])
                    else:
                        def_evaluate(evaluate[4])
    else:
        if def_problem(problem[7]):
            if def_problem(problem[9]):
                if def_problem(problem[15]):
                    if def_problem(problem[16]):
                        if def_problem(problem[17]):
                            if def_problem(problem[18]):
                                if def_problem(problem[19]):
                                    def_evaluate(evaluate[15])
                                else:
                                    if def_problem(problem[20]):
                                        def_evaluate(evaluate[16])
                                    else:
                                        if def_problem(problem[21]):
                                            def_evaluate(evaluate[18])
                                        else:
                                            def_evaluate(evaluate[17])
                            else:
                                if def_problem(problem[22]):
                                    def_evaluate(evaluate[19])
                                else:
                                    def_evaluate(evaluate[20])
                        else:
                            def_evaluate(evaluate[14])
                    else:
                        if def_problem(problem[23]):
                            def_evaluate(evaluate[21])
                        else:
                            if def_problem(problem[24]):
                                if def_problem(problem[25]):
                                    if def_problem(problem[26]):
                                        if def_problem(problem[27]):
                                            def_evaluate(evaluate[26])
                                        else:
                                            def_evaluate(evaluate[25])
                                    else:
                                        def_evaluate(evaluate[24])
                                else:
                                    def_evaluate(evaluate[23])
                            else:
                                def_evaluate(evaluate[22])
                else:
                    if def_problem(problem[28]):
                        if def_problem(problem[29]):
                            if def_problem(problem[30]):
                                def_evaluate(evaluate[29])
                            else:
                                def_evaluate(evaluate[28])
                        else:
                            def_evaluate(evaluate[27])
                    else:
                        if def_problem(problem[31]):
                            if def_problem(problem[34]):
                                def_evaluate(evaluate[33])
                            else:
                                if def_problem(problem[35]):
                                    if def_problem(problem[36]):
                                        def_evaluate(evaluate[35])
                                    else:
                                        if def_problem(problem[37]):
                                            def_evaluate(evaluate[36])
                                        else:
                                            def_evaluate(evaluate[37])
                                else:
                                    def_evaluate(evaluate[34])
                        else:
                            if def_problem(problem[32]):
                                def_evaluate(evaluate[30])
                            else:
                                if def_problem(problem[33]):
                                    def_evaluate(evaluate[31])
                                else:
                                    def_evaluate(evaluate[32])
            else:
                if def_problem(problem[10]):
                    if def_problem(problem[11]):
                        def_evaluate(evaluate[10])
                    else:
                        if def_problem(problem[12]):
                            def_evaluate(evaluate[11])
                        else:
                            if def_problem(problem[13]):
                                if def_problem(problem[14]):
                                    def_evaluate(evaluate[13])
                                else:
                                    def_evaluate(evaluate[12])
                            else:
                                def_evaluate(evaluate[12])
                else:
                    def_evaluate(evaluate[9])
        else:
            if def_problem(problem[8]):
                def_evaluate(evaluate[7])
            else:
                def_evaluate(evaluate[8])
