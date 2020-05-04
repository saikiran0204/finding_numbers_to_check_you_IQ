import tkinter
from turtle import *
from random import randrange
from time import sleep
from datetime import datetime


class Players:
    def __init__(self, name):
        time = datetime.now()
        self.name = name
        self.points = 0
        self.time = datetime.now() - time
        self.time_in_each_round = []
        self.position_turtle = []


def draw(limit):
    global position
    for i in range(limit):
        a = True
        while a:
            a = False
            x = randrange(-800, 200)
            y = randrange(-400, 400)
            for j in position.keys():
                if 500 > (position[j][0] - x) ** 2 + (position[j][1] - y) ** 2:
                    a = True
                    break
        setposition(x, y)
        position[i] = [x, y]
        write(i, align='center')


def show(number):
    global position
    setposition(position[number])
    pendown()
    circle(13)
    penup()


def round(number):
    setposition(360, 380)
    fillcolor('White')
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(30)
        else:
            forward(15)
        left(90)
    end_fill()
    setposition(363, 380)
    write(number)


def click(x, y):
    global position, number_to_find, i, players, starting_time, number_of_players
    person = i % number_of_players
    if 500 > (position[number_to_find][0] - x) ** 2 + (position[number_to_find][1] - y) ** 2:
        print("Found")
        Round = i // number_of_players
        time_taken = datetime.now() - starting_time
        if Round == 0 or players[person].time is None:
            players[person].time = time_taken
        else:
            players[person].time += time_taken
        players[person].points += 1
        players[person].time_in_each_round[Round] = time_taken
        erase_turn(players[person].position_turtle)
        erase_time(players[person].position_turtle, time_taken)
        print("Time taken:", time_taken)
        i += 1
        turn()
    elif 900 > (x - 300) ** 2 + (y + 200) ** 2:
        show(number_to_find)
        setposition(300, -272)
        write('check for 5 seconds')
        sleep(5)
        backward(3)
        fillcolor('White')
        begin_fill()
        for j in range(4):
            if j % 2 == 0:
                forward(100)
            else:
                forward(15)
            left(90)
        end_fill()
        erase_time(players[person].position_turtle, '----')
        erase_turn(players[person].position_turtle)
        i += 1
        turn()
    elif 900 > (x - 400) ** 2 + (y + 200) ** 2:
        Screen().bye()
        sort_and_final()
    else:
        print("out")


def clear_screen():
    fillcolor('White')
    begin_fill()
    setposition(-810, 410)
    setposition(-810, -410)
    setposition(210, -410)
    setposition(210, 410)
    setposition(-810, 410)
    end_fill()


def turn():
    clear_screen()
    global i, number_to_find, players, starting_time, position, number_of_players, number_of_rounds
    Round = i // number_of_players
    if Round == number_of_rounds:
        Screen().bye()
        sort_and_final()
    if i % number_of_players == 0:
        round(Round + 1)
    limit = 100 * (Round + 1)  # change the limit here
    position = {}
    player_turn = i % number_of_players
    setposition(players[player_turn].position_turtle)
    write('-->')
    draw(limit)
    number_to_find = randrange(limit)
    print("player", players[player_turn].name, "to find ", number_to_find)
    find_number(number_to_find)
    starting_time = datetime.now()
    #show(number_to_find)
    onscreenclick(click)


def find_number(number):
    setposition(357, -100)
    fillcolor('White')
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(30)
        else:
            forward(15)
        left(90)
    end_fill()
    setposition(360, -100)
    write(number)


def sort_and_final():
    global players, number_of_players, number_of_rounds, z
    for i in range(number_of_players):
        for j in range(i + 1, number_of_players):
            if (players[j].points > players[i].points) or (
                    players[i].points == players[j].points and players[i].time > players[j].time):
                players[i], players[j] = players[j], players[i]
    z = tkinter.Tk()
    tkinter.Label(z, text='Sno').grid(row=0, column=0)
    tkinter.Label(z, text='Name').grid(row=0, column=1)
    for i in range(number_of_rounds):
        tkinter.Label(z, text='Round' + str(i + 1)).grid(row=0, column=2 + i)
    tkinter.Label(z, text="Total time").grid(row=0, column=i + 3)
    for i in range(number_of_players):
        tkinter.Label(z, text=str(i + 1) + ')').grid(row=i + 1, column=0)
        tkinter.Label(z, text=players[i].name).grid(row=i + 1, column=1)
        for j in range(number_of_rounds):
            tkinter.Label(z, text=str(players[i].time_in_each_round[j])[3:]).grid(row=i + 1, column=j + 2)
        tkinter.Label(z, text=str(players[i].time)[2:]).grid(row=i + 1, column=j + 3)
    tkinter.Button(z, text='close', command=lambda: close()).grid(row=number_of_players + 2,
                                                                  column=2 + int(number_of_rounds / 2))
    z.mainloop()


def close():
    global z
    z.destroy()
    exit()


def erase_turn(x):
    setposition(x[0] - 3, x[1] + 1)
    fillcolor('White')
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(20)
        else:
            forward(10)
        left(90)
    end_fill()


def erase_time(x, time_taken):
    setposition(x[0] + 138, x[1] + 1)
    fillcolor('White')
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(80)
        else:
            forward(12)
        left(90)
    end_fill()
    setposition(x[0] + 140, x[1])
    write(time_taken)


def setup_turtle():
    speed(0)
    penup()
    setposition(210, -410)
    pendown()
    pensize(5)
    setposition(210, 410)
    pendown()
    pensize(1)
    penup()
    hideturtle()
    global number_of_players, players
    # screensize(1200, 1000, 'white')
    setposition(326, 380)
    write('Round')
    x = 250
    y = 350
    setposition(250, 350)
    write("turn")
    setposition(x + 70, y)
    write("name")
    setposition(x + 140, y)
    write("time taken for privous turn")
    for i in range(number_of_players):
        k = y - (i + 1) * 20
        players[i].position_turtle = [x, k]
        setposition(x + 70, k)
        write(players[i].name)
        setposition(x + 140, k)
        write("----")
    setposition(300, -200)
    write("Not found", align='center')
    setposition(300, -230)
    pendown()
    circle(30)
    penup()
    setposition(400, -200)
    write("End Game", align='center')
    setposition(400, -230)
    pendown()
    circle(30)
    penup()
    setposition(295, -100)
    write('Find number:')
    turn()
    mainloop()


def third(players_entry):
    global players, number_of_players, number_of_rounds
    for i in range(number_of_players):
        players.append(Players(players_entry[i].get()))
        players[i].time_in_each_round = ['------'] * number_of_rounds
    t.destroy()
    setup_turtle()


def second(no_of_players, rounds):
    global number_of_players, number_of_rounds
    players_entry = []
    number_of_players = int(no_of_players.get())
    number_of_rounds = int(rounds.get())
    frame1.destroy()
    for i in range(number_of_players):
        tkinter.Label(frame2, text="enter player " + str(i + 1) + " name:").grid(row=i, column=0)
        players_entry.append(tkinter.Entry(frame2))
        players_entry[i].grid(row=i, column=1)
    tkinter.Button(frame2, text='Click to start', command=lambda players=players_entry: third(players)).grid(
        row=number_of_players + 1, column=1)


def first():
    tkinter.Label(frame1, text="Enter number of rounds").grid(row=0, column=0)
    number_of_rounds = tkinter.Entry(frame1)
    number_of_rounds.grid(row=0, column=1)
    tkinter.Label(frame1, text="Enter number of players").grid(row=1, column=0)
    number_of_players = tkinter.Entry(frame1)
    number_of_players.grid(row=1, column=1)
    tkinter.Button(frame1, text="next",
                   command=lambda players=number_of_players, rounds=number_of_rounds: second(number_of_players,
                                                                                             number_of_rounds)).grid(
        row=3, column=1)


players = []
position = {}
i = 0
starting_time = 0
number_to_find = 0
number_of_rounds = 0
number_of_players = 0
t = tkinter.Tk()
t.title("Finding Numbers")
frame1 = tkinter.Frame(t)
frame2 = tkinter.Frame(t)
first()
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
t.mainloop()
