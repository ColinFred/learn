#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Tic_Tac_Toe import gameover, comwin, userwin


class TreeNode:
    def __init__(self, checkboard):
        # 记录当前棋盘
        self.board = checkboard
        # 当前节点的评估值
        self.val = None


def get_val(Board):
    """
    获取当前节点的评估值
    """
    base_board = []
    number = 0
    for j in range(3):
        base_board.append([Board[i + j * 3] for i in range(3)])

    board = base_board[:]
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1

    if board[0][0] + board[1][1] + board[2][2] == -3:
        number += 1
    if board[2][0] + board[1][1] + board[0][2] == -3:
        number += 1
    for i in range(3):
        if board[i][0] + board[i][1] + board[i][2] == -3:
            number += 1
        if board[0][i] + board[1][i] + board[2][i] == -3:
            number += 1

    board = base_board[:]
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1

    if board[0][0] + board[1][1] + board[2][2] == 3:
        number -= 1
    if board[2][0] + board[1][1] + board[0][2] == 3:
        number -= 1
    for i in range(3):
        if board[i][0] + board[i][1] + board[i][2] == 3:
            number -= 1
        if board[0][i] + board[1][i] + board[2][i] == 3:
            number -= 1

    return number


class get_next_step:
    def start(self, checkboard, deep):
        self.deep = deep  # 记录节点深度
        self.return_value = None  # 记录最优解
        self.get_max_or_min(deep, checkboard)  # 递归求解
        return self.return_value  # 返回最优解

    def get_max_or_min(self, deep, board):
        if comwin(board):
            return 50
        if userwin(board):
            return -50
        if gameover(board):
            return 0
        if deep == 0:
            return get_val(board)
        # 依次求极大值和极小值
        if (self.deep - deep) % 2 == 0:
            Max = -50
            location = 0
            for i in range(9):
                if board[i] == 0:
                    # 更新棋盘
                    copy_checkboard = board[:]
                    copy_checkboard[i] = -1
                    # 对新的棋盘建立新的节点
                    treenode = TreeNode(copy_checkboard)
                    # 此节点的评估值等于所有子节点中的最小评估值
                    treenode.val = self.get_max_or_min(deep - 1, copy_checkboard)
                    # 比较同一层次的节点，返回评估值最大的节点的评估值和其落子位置
                    if treenode.val > Max:
                        location, Max = i, treenode.val
                self.return_value = location
            return Max
        else:
            Min = 50
            for i in range(9):
                if board[i] == 0:
                    # 更新棋盘
                    copy_checkboard = board[:]
                    copy_checkboard[i] = 1
                    # 根据新的棋盘建立新的节点
                    treenode = TreeNode(copy_checkboard)
                    # 此节点的评估值等于所有子节点中的最大评估值
                    treenode.val = self.get_max_or_min(deep - 1, copy_checkboard)
                    # 比较同一层次的节点，返回评估值最小的节点的评估值和其落子位置
                    if treenode.val < Min:
                        Min = treenode.val
            return Min
