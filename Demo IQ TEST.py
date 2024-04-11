# Demo IQ Test
import tkinter
from tkinter import *
import time


def close():
    leaderboard_screen.destroy()


def goback():
    leaderboard_screen.destroy()
    results_screen.destroy()
    main_page()


class Порядковый_номер:
    pass


def leaderboard():
    global leaderboard_screen
    leaderboard_screen = Tk()
    leaderboard_screen.geometry = "500x500"
    leaderboard_screen.resizable(False, False)
    leaderboard_screen.title("Таблица лидеров")

    k = open("results.txt", "r")
    x = k.readlines()
    h = []
    for i in x:
        stats = i.split()
        if (len(stats) > 4):
            for j in range(len(stats) - 4):
                stats[0] = stats[0] + " " + stats[1]
                stats.pop(1)
        h.append(stats)

    Label(leaderboard_screen, text="Таблица лидеров", font="10", bg="black", fg="white", width="25", height="3").grid(
        column=1, row=0)
    Label(leaderboard_screen, text="").grid()
    # Label(leaderboard_screen, text="Имя                 Порядковый номер                  Score", font=("arial 15 bold"), padx="30").grid()
    Label(leaderboard_screen, text="Имя", font=("arial 15 bold"), padx="30").grid(column=0, row=1)
    Label(leaderboard_screen, text="Порядковый номер", font=("arial 15 bold"), padx="30").grid(column=1, row=1)
    Label(leaderboard_screen, text="Счёт", font=("arial 15 bold"), padx="30").grid(column=2, row=1)
    Label(leaderboard_screen, text="").grid()

    score = []
    for i in range(len(h)):
        if (len(h[i]) == 0):
            h.pop(i)
            continue
        score.append(int(h[i][2]))

    stats = []
    rownum = 2
    for i in range(len(h)):
        x = score.index(max(score))
        stats = h[x]
        score.pop(x)
        h.pop(x)
        Имя = stats[0]
        Номер = stats[1]
        Счёт = stats[2]
        Label(leaderboard_screen, text=Имя, font=("arial 11")).grid(column=0, row=rownum)
        Label(leaderboard_screen, text=Порядковый_номер, font=("arial 11")).grid(column=1, row=rownum)
        Label(leaderboard_screen, text=Счёт, font=("arial 11")).grid(column=2, row=rownum)
        rownum = rownum + 1

    Label(leaderboard_screen, text="").grid()
    Button(leaderboard_screen, text="Закрыть", font=("Algerian 10"), bg="grey", fg="white", command=close).grid(column=1,
                                                                                                              row=rownum + 2)
    Button(leaderboard_screen, text="Home Page", font=("Algerian 10"), bg="grey", fg="white", command=goback).grid(
        column=2, row=rownum + 2)


def showresults():
    global results_screen
    ques10_screen.destroy()
    results_screen = Tk()
    results_screen.geometry = "300x300"
    results_screen.resizable(False, False)
    results_screen.title("RESULTS")

    Label(results_screen, text="Ваши результаты", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(results_screen, text="").pack()
    Label(results_screen, text="У вас есть", font=5).pack()
    Label(results_screen, text=NUM_RIGHT_ANS + " Правильных ответов", fg="green", font=10).pack()
    x = 10 - int(NUM_RIGHT_ANS)
    x = str(x)
    Label(results_screen, text=x + " Неправильных ответов", fg="red", font=10).pack()
    Label(results_screen, text="").pack()
    Label(results_screen, text="Ваш балл равен " + total_ans + "/1400", font=("arial 20 italic"), bg="yellow").pack()
    Label(results_screen, text="").pack()
    Button(results_screen, text="Таблица лидеров", font=("arial 10 italic"), bg="black", fg="white", padx="25",
           command=leaderboard).pack(anchor=E)
    Label(results_screen, text="").pack()


def store_stats():
    global total_ans
    total_ans = maxcount + maxcount1 + maxcount2 + maxcount3 + maxcount4 + maxcount5 + maxcount6 + maxcount7 + maxcount8 + maxcount9
    total_ans = str(total_ans)

    global NUM_RIGHT_ANS
    NUM_RIGHT_ANS = anscount1 + anscount2 + anscount3 + anscount4 + anscount5 + anscount6 + anscount7 + anscount8 + anscount9 + anscount10
    NUM_RIGHT_ANS = str(NUM_RIGHT_ANS)

    f = open("results.txt", "a")
    f.write(UserName + "  ")
    f.write(EntryNum + "  ")
    f.write(total_ans + "  ")
    f.write(NUM_RIGHT_ANS)
    f.write("\n")

    showresults()


def first_assign():
    global maxcount
    maxcount = IntVar()
    maxcount = M[-1]

    global anscount1
    anscount1 = IntVar()
    if (maxcount > 10):
        anscount1 = 1
    else:
        anscount1 = 0
    ques2()


def second_assign():
    global maxcount1
    maxcount1 = IntVar()
    maxcount1 = M[-1]

    global anscount2
    anscount2 = IntVar()
    if (maxcount1 > 10):
        anscount2 = 1
    else:
        anscount2 = 0
    ques3()


def third_assign():
    global maxcount2
    maxcount2 = IntVar()
    maxcount2 = M[-1]

    global anscount3
    anscount3 = IntVar()
    if (maxcount2 > 10):
        anscount3 = 1
    else:
        anscount3 = 0
    ques4()


def fourth_assign():
    global maxcount3
    maxcount3 = IntVar()
    maxcount3 = M[-1]

    global anscount4
    anscount4 = IntVar()
    if (maxcount3 > 10):
        anscount4 = 1
    else:
        anscount4 = 0
    ques5()


def fifth_assign():
    global maxcount4
    maxcount4 = IntVar()
    maxcount4 = M[-1]

    global anscount5
    anscount5 = IntVar()
    if (maxcount4 > 10):
        anscount5 = 1
    else:
        anscount5 = 0
    ques6()


def sixth_assign():
    global maxcount5
    maxcount5 = IntVar()
    maxcount5 = M[-1]

    global anscount6
    anscount6 = IntVar()
    if (maxcount5 > 10):
        anscount6 = 1
    else:
        anscount6 = 0
    ques7()


def seventh_assign():
    global maxcount6
    maxcount6 = IntVar()
    maxcount6 = M[-1]

    global anscount7
    anscount7 = IntVar()
    if (maxcount6 > 10):
        anscount7 = 1
    else:
        anscount7 = 0
    ques8()


def eighth_assign():
    global maxcount7
    maxcount7 = IntVar()
    maxcount7 = M[-1]

    global anscount8
    anscount8 = IntVar()
    if (maxcount7 > 10):
        anscount8 = 1
    else:
        anscount8 = 0
    ques9()


def ninth_assign():
    global maxcount8
    maxcount8 = IntVar()
    maxcount8 = M[-1]

    global anscount9
    anscount9 = IntVar()
    if (maxcount8 > 10):
        anscount9 = 1
    else:
        anscount9 = 0
    ques10()


def tenth_assign():
    global maxcount9
    maxcount9 = IntVar()
    maxcount9 = M[-1]

    global anscount10
    anscount10 = IntVar()
    if (maxcount9 > 10):
        anscount10 = 1
    else:
        anscount10 = 0
    store_stats()


def ques1():
    global ques1_screen
    detailscreen.destroy()
    ques1_screen = Tk()
    ques1_screen.geometry("600x600")
    ques1_screen.title("Вопрос 1")
    ques1_screen.resizable(False, False)

    global v
    v = IntVar()
    global M
    M = []

    Label(ques1_screen, text="Вопрос 1", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques1_screen, text="").pack()
    Label(ques1_screen, text="Какой из этих городов лишний? \n"
                             " Москва, Мадрид, Карас, Лондон", font="7").pack()
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text='Москва', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text="Мадрид", value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text="Карас", value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(100)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    Radiobutton(ques1_screen, text="Лондон", value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques1_screen, text="").pack()
    btn = Button(ques1_screen, text="Далее", font="1", fg="white", bg="black", command=first_assign).pack()
    Label(ques1_screen, text="").pack()


def ques2():
    global ques2_screen
    ques1_screen.destroy()
    ques2_screen = Tk()
    ques2_screen.geometry("600x600")
    ques2_screen.title("Вопрос 2")
    ques2_screen.resizable(False, False)

    global v
    v = IntVar()
    global M
    M = []

    Label(ques2_screen, text="Вопрос 2", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques2_screen, text="").pack()
    Label(ques2_screen, text=" Какое число лишнее? \n"
                             "1, 3, 5, 6", font="7").pack()
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='6', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(150)).pack(anchor=W)
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='3', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='5', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques2_screen, text="").pack()
    Radiobutton(ques2_screen, text='1', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Button(ques2_screen, text="Далее", font="1", fg="white", bg="black", command=second_assign).pack()
    Label(ques2_screen, text="").pack()


def ques3():
    global ques3_screen
    ques2_screen.destroy()
    ques3_screen = Tk()
    ques3_screen.geometry("600x600")
    ques3_screen.title("Вопрос 3")
    ques3_screen.resizable(False, False)

    Label(ques3_screen, text="Вопрос 3", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques3_screen, text="").pack()
    Label(ques3_screen, text=" Какие из перечисленных стран расположены в Южной Америке? \n", font="5").pack()
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Япония', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Индия', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Австралия', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques3_screen, text="").pack()
    Radiobutton(ques3_screen, text='Чили', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(100)).pack(anchor=W)
    Button(ques3_screen, text="Далее", font="1", fg="white", bg="black", command=third_assign).pack()
    Label(ques3_screen, text="").pack()


def ques4():
    global ques4_screen
    ques3_screen.destroy()
    ques4_screen = Tk()
    ques4_screen.geometry("600x600")
    ques4_screen.title("Вопрос 4")
    ques4_screen.resizable(False, False)

    Label(ques4_screen, text="Вопрос 4", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques4_screen, text="").pack()
    Label(ques4_screen, text=" Какое число следует в последовательности: 8, 13, 21, 34 \n", font="7").pack()
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='89', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='44', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='61', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques4_screen, text="").pack()
    Radiobutton(ques4_screen, text='55', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(200)).pack(anchor=W)
    Button(ques4_screen, text="Далее", font="1", fg="white", bg="black", command=fourth_assign).pack()
    Label(ques4_screen, text="").pack()


def ques5():
    global ques5_screen
    ques4_screen.destroy()
    ques5_screen = Tk()
    ques5_screen.geometry("600x600")
    ques5_screen.title("Вопрос 5")
    ques5_screen.resizable(False, False)

    Label(ques5_screen, text="Вопрос 5", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques5_screen, text="").pack()
    Label(ques5_screen, text="Какое из перечисленных утверждений является истинным? \n", font="7").pack()
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='Все лошади - животные', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='Некоторые лошади - животные', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(100)).pack(anchor=W)
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='Все животные - лошади', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques5_screen, text="").pack()
    Radiobutton(ques5_screen, text='Никто из лошадей не является животным', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Button(ques5_screen, text="Далее", font="1", fg="white", bg="black", command=fifth_assign).pack()
    Label(ques5_screen, text="").pack()


def ques6():
    global ques6_screen
    ques5_screen.destroy()
    ques6_screen = Tk()
    ques6_screen.geometry("900x500")
    ques6_screen.title("Вопрос 6")
    ques6_screen.resizable(False, False)

    Label(ques6_screen, text="Вопрос 6", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques6_screen, text="").pack()
    Label(ques6_screen, text="Если в слове ПАРАДОКС переставить буквы местами, какое слово получится? \n", font="7").pack()
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='РАСПОДАК', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='КРОДПААС', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(150)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='СКРАДПАО', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Radiobutton(ques6_screen, text='КОДПРАСА', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques6_screen, text="").pack()
    Button(ques6_screen, text="Далее", font="1", fg="white", bg="black", command=sixth_assign).pack()
    Label(ques6_screen, text="").pack()


def ques7():
    global ques7_screen
    ques6_screen.destroy()
    ques7_screen = Tk()
    ques7_screen.geometry("600x600")
    ques7_screen.title("Вопрос 7")
    ques7_screen.resizable(False, False)

    Label(ques7_screen, text="Вопрос 7", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques7_screen, text="").pack()
    Label(ques7_screen, text="Какое из перечисленных животных не относится к кошачьим? \n", font="7").pack()
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='Леопард', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='Тигр', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='Пума', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Radiobutton(ques7_screen, text='Лев', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(200)).pack(anchor=W)
    Label(ques7_screen, text="").pack()
    Button(ques7_screen, text="Далее", font="1", fg="white", bg="black", command=seventh_assign).pack()
    Label(ques7_screen, text="").pack()


def ques8():
    global ques8_screen
    ques7_screen.destroy()
    ques8_screen = Tk()
    ques8_screen.geometry("700x600")
    ques8_screen.title("Вопрос 8")
    ques8_screen.resizable(False, False)

    Label(ques8_screen, text="Вопрос 8", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques8_screen, text="").pack()
    Label(ques8_screen, text="Какое животное из списка обладает наименьшим количеством ног \n", font="7").pack()
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='Паук', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='Скорпион', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='Эму', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(50)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Radiobutton(ques8_screen, text='Слон', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques8_screen, text="").pack()
    Button(ques8_screen, text="Далее", font="1", fg="white", bg="black", command=eighth_assign).pack()
    Label(ques8_screen, text="").pack()


def ques9():
    global ques9_screen
    ques8_screen.destroy()
    ques9_screen = Tk()
    ques9_screen.geometry("700x600")
    ques9_screen.title("Вопрос 9")
    ques9_screen.resizable(False, False)

    Label(ques9_screen, text="Вопрос 9", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques9_screen, text="").pack()
    Label(ques9_screen, text="Какое из перечисленных слов не соответсвует остальным по смыслу? \n", font="7").pack()
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='Лимон', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(200)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='Апельсин', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='Банан', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Radiobutton(ques9_screen, text='Яблоко', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques9_screen, text="").pack()
    Button(ques9_screen, text="Далее", font="1", fg="white", bg="black", command=ninth_assign).pack()
    Label(ques9_screen, text="").pack()


def ques10():
    global ques10_screen
    ques9_screen.destroy()
    ques10_screen = Tk()
    ques10_screen.geometry("800x800")
    ques10_screen.title("Вопрос 10")
    ques10_screen.resizable(False, False)

    Label(ques10_screen, text="Вопрос 10", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(ques10_screen, text="").pack()
    Label(ques10_screen, text=" Если в 3:00 назовут 300 курантов, сколько курантов осведомят вас о времени в 6:45?? \n", font="7").pack()
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='600', value=1, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(250)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='675', value=2, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='700', value=3, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Radiobutton(ques10_screen, text='750', value=4, padx="80", font=("arial", 15, "italic"),
                command=lambda: M.append(0)).pack(anchor=W)
    Label(ques10_screen, text="").pack()
    Button(ques10_screen, text="Отправить", font="1", fg="white", bg="black", command=tenth_assign).pack()
    Label(ques10_screen, text="").pack()


def details():
    global detailscreen
    loginscreen.destroy()
    detailscreen = Tk()
    detailscreen.geometry = "500x500"
    detailscreen.title("Правила")
    detailscreen.resizable(False, False)

    Label(detailscreen, text="Правила", font="10", bg="black", fg="white", width="50", height="3").pack()
    Label(detailscreen, text="").pack()
    Label(detailscreen, text="Теперь вам предстоит ответить на 10 вопросов \n "
                             "в течении 10 минут \n", font="7").pack()
    Label(detailscreen, text="").pack()
    Label(detailscreen, text="*Каждый вопрос является обязательным\n\n"
                             "*Если вы перейдёте к следующему вопросу, вы не сможете вернуться", fg="red").pack()
    Label(detailscreen, text="").pack()
    Label(detailscreen, text="Всего наилучшего!", font="7", fg="blue").pack()
    Label(detailscreen, text="").pack()
    Button(detailscreen, text="Начать", font="1", fg="white", bg="black", command=ques1).pack()
    Label(detailscreen, text="").pack()


def check_validity_entrynum():
    global EntryNum
    EntryNum = entrynum.get()

    if (entrynum.get() == ""):
        loginscreen.destroy()
        login_page()
    else:
        details()


def check_validity_username():
    global UserName
    UserName = username.get()

    if (UserName == ""):
        loginscreen.destroy()
        login_page()
    else:
        check_validity_entrynum()


def mainpage_to_loginpage():
    mainscreen.destroy()
    login_page()


def login_page():
    global loginscreen
    loginscreen = Tk()
    loginscreen.geometry = "500x500"
    loginscreen.title("Авторизация")
    loginscreen.resizable(False, False)

    global username
    global entrynum
    username = StringVar()
    entrynum = StringVar()

    Label(loginscreen, text="Авторизация", font="10", bg="black", fg="white", width="40", height="3").pack()

    Label(loginscreen, text="").pack()
    Label(loginscreen, text="Имя", font="7").pack()
    Entry(loginscreen, font="2", textvariable=username, width=26).pack()
    Label(loginscreen, text="").pack()
    Label(loginscreen, text="Порядковый номер", font="7").pack()
    Entry(loginscreen, font="2", textvariable=entrynum, width=26).pack()
    Label(loginscreen, text="").pack()

    Button(loginscreen, text="Далее", font="5", bg="grey", fg="black", command=check_validity_username).pack()
    Label(loginscreen, text="").pack()


def main_page():
    global mainscreen
    mainscreen = Tk()
    mainscreen.geometry = "500x500"
    mainscreen.title("IQ TEST")
    mainscreen.resizable(False, False)

    Label(mainscreen, text="Добро Пожаловать на IQ TEST", font="1", bg="black", fg="white", width="50", height="3").pack()

    Label(mainscreen, text="").pack()
    Label(mainscreen, text="Тест состоит из 10 вопросов",
          font="3").pack()

    Label(mainscreen, text="").pack()
    Label(mainscreen, text="").pack()
    Button(mainscreen, text="НАЧАТЬ", font="5", bg="grey", fg="black", command=mainpage_to_loginpage).pack()
    Label(mainscreen, text="").pack()
    mainscreen.mainloop()


main_page()