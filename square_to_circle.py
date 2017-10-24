#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# form collections import Iterable
import turtle

def draw_square():
    # 创建红色背景的窗口
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('triangle') #箭头形状
    brad.color('blue') #箭头颜色
    brad.speed(5) #箭头速度

    j = 0
    while j < (360/10):
        i = 0
        while i < 4:
            # 先前走100步
            brad.forward(100)
            # 右转90度
            brad.right(90)
            i += 1
        j += 1
        brad.right(10)

    # 画一个圆形
    # circy = turtle.Turtle()
    # brad.shape('arrow')  # 箭头形状
    # brad.color('yellow')  # 箭头颜色
    # circy.circle(100)

    # 点击关闭
    window.exitonclick()

draw_square()
