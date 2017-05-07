#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from computer import get_next_step


def checkboard_2_status1(checkBoard):
    """
    转化为棋盘
    >>> checkboard = [0, 0, 0, 0, 1, -1, 0, 0, 0]
    >>> checkboard_2_status1()
    ['  ', '  ', '  ', '  ', '○', '×', '  ', '  ', '  ']
    """
    Status1 = ['  '] * 9
    for i in range(9):
        if checkBoard[i] == 1:
            Status1[i] = '○'
        elif checkBoard[i] == -1:
            Status1[i] = '×'
    return Status1


def checkboard_2_status2(checkBoard):
    """
    转化为数字键盘，用来控制键盘，禁止输入的数字用'-'表示
    >>> checkBoard = [0, 0, 0, 0, 1, -1, 0, 0, 0]
    >>> checkboard_2_status2()
    ['1', '2', '3', '4', '-', '-', '7', '8', '9']
    """
    Status2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(9):
        if checkBoard[i] != 0:
            Status2[i] = '-'
    return Status2


def printf1(checkBoard):
    """
    显示棋盘
    """
    Status1, Status2 = checkboard_2_status1(checkBoard), checkboard_2_status2(checkBoard)
    print("                                                               ")
    print("                      井字棋——人机对弈                       ")
    print("                                          您：○   电脑：×    ")
    print("       {} | {} | {}                       请输入数字在棋盘摆放位置（输入 0 退出）".format(Status1[0], Status1[1], Status1[2]))
    print("      ———————                                           ")
    print("       {} | {} | {}                       {}  {}  {} ".format(Status1[3], Status1[4], Status1[5], Status2[0],
                                                                         Status2[1], Status2[2]))
    print("      ———————                      {}  {}  {} ".format(Status2[3], Status2[4], Status2[5]))
    print("       {} | {} | {}                       {}  {}  {} ".format(Status1[6], Status1[7], Status1[8], Status2[6],
                                                                         Status2[7], Status2[8]))
    print("                                                               ")


def printf2(checkBoard):
    """
    显示棋盘
    """
    Status1, Status2 = checkboard_2_status1(checkBoard), checkboard_2_status2(checkBoard)
    print("                                                               ")
    print("                      井字棋——人机对弈                       ")
    print("                                          您：○   电脑：×    ")
    print("       {} | {} | {}                       现在是电脑思考时间".format(Status1[0], Status1[1], Status1[2]))
    print("      ———————                                           ")
    print("       {} | {} | {}                       ".format(Status1[3], Status1[4], Status1[5]))
    print("      ———————                                           ")
    print("       {} | {} | {}                       ".format(Status1[6], Status1[7], Status1[8]))
    print("                                                               ")


def getinput_by_user(checkBoard):
    """
    获取用户输入
    """
    print("您的走法是： ")
    num = input()
    while num < '0' or num > '9':
        print("数字越界，请重新输入 ")
        num = input()
    if num == '0':
        os._exit(0)
    num = int(num)
    while checkBoard[num - 1] != 0:
        print("该位置已有棋子，请重新输入")
        num = int(input("您的走法是： "))
    return num


def getinput_by_com_easy(checkBoard):
    """
     获取电脑输入__简单
    """
    deep = 1
    Iwanna = get_next_step()
    return Iwanna.start(checkBoard, deep) + 1


def getinput_by_com_middle(checkBoard):
    """
    获取电脑输入__中等
    """
    deep = 2
    Iwanna = get_next_step()
    return Iwanna.start(checkBoard, deep) + 1


def getinput_by_com_hard(checkBoard):
    """
    获取电脑输入__困难
    """
    deep = 3
    Iwanna = get_next_step()
    return Iwanna.start(checkBoard, deep) + 1


def update_checkboard(checkBoard, who, mode):
    """
    更新棋盘状态
    每次调用轮流读取电脑和用户的输入
    """
    user, com = 1, -1
    player = user if who == '1' else com
    if mode == '1':
        get_input_by_com = getinput_by_com_easy
    elif mode == '2':
        get_input_by_com = getinput_by_com_middle
    else:
        get_input_by_com = getinput_by_com_hard
    location = getinput_by_user(checkBoard) if player == user else get_input_by_com(checkBoard)
    checkBoard[location - 1] = player


def checkboard_2_board(checkBoard):
    """
    >>> checkBoard = [0, 0, 0, 0, 1, -1, 0, 0, 0]
    >>> checkboard_2_board()
    [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
    """
    board = []
    for j in range(3):
        board.append([checkBoard[i + j * 3] for i in range(3)])
    return board


def anyonewin(checkBoard):
    if comwin(checkBoard):
        printf1(checkBoard)
        print("抱歉，你输了。")
        print(" ")
        return True
    if userwin(checkBoard):
        printf1(checkBoard)
        print("恭喜你，你赢了！")
        print(" ")
        return True
    if gameover(checkBoard):
        printf1(checkBoard)
        print("游戏结束——平局")
        print(" ")
        return True
    return False


def comwin(checkBoard):
    board = checkboard_2_board(checkBoard)
    if board[0][0] + board[1][1] + board[2][2] == -3:
        return True
    if board[2][0] + board[1][1] + board[0][2] == -3:
        return True
    for i in range(3):
        if board[i][0] + board[i][1] + board[i][2] == -3 or board[0][i] + board[1][i] + board[2][i] == -3:
            return True
    return False


def userwin(checkBoard):
    board = checkboard_2_board(checkBoard)
    if board[0][0] + board[1][1] + board[2][2] == 3:
        return True
    if board[2][0] + board[1][1] + board[0][2] == 3:
        return True
    for i in range(3):
        if board[i][0] + board[i][1] + board[i][2] == 3 or board[0][i] + board[1][i] + board[2][i] == 3:
            return True
    return False


def gameover(checkBoard):
    for i in checkBoard:
        if i == 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        checkBoard = [0]*9
        print("请选择模式")
        print("简单： 1    "
              "中等： 2    "
              "困难： 3    ")
        mode = input()
        while mode != '1' and mode != '2' and mode != '3':
            print("输入 1 ， 2 或 3 ")
            mode = input()
        print("请选择先手还是后手")
        print("先手： 1    "
              "后手： 2    ")
        who = input()
        while who != '1' and who != '2':
            print("输入 1 或 2 ")
            who = input()
        notDone = 1
        while notDone:
            if who == '1':
                printf1(checkBoard)
                update_checkboard(checkBoard, who, mode)
                who = '2'
            else:
                printf2(checkBoard)
                time.sleep(1)
                update_checkboard(checkBoard, who, mode)
                who = '1'
            if anyonewin(checkBoard):
                notDone = 0

        print("回车继续，输入 0 退出")
        restart = input()
        print(" ")
        if restart == '0':
            break
