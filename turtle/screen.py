# Portions of this code are taken from https://github.com/PRAISE-group/Chiron-Framework/blob/master/ChironCore/interpreter.py
# (from the Chiron Framework) and are licensed as follows:
#
# MIT License
#
# Copyright (c) 2022 Subhajit Roy, Prantik Chaterjee, Gourav Takhar, Sujit Muduli, Pankaj Kalita, Sumit Lahiri,  Vishal Singh
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import turtle

class Screen:
    '''
    Turtle graphics interface for the SPIM simulator.

    The simulator can use this class to control turtle graphics without
    directly interacting with the turtle module. How instructions can
    signal the simulator to use this interface is up to the simulator
    design.
    '''

    def __init__(self):
        self.screen = turtle.getscreen()
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("blue", "yellow")
        self.turtle.fillcolor("green")
        self.turtle.begin_fill()
        self.turtle.pensize(4)
        self.turtle.speed(1)  # TODO: Make it user friendly

        turtle.title("SPIM Turtle")
        turtle.bgcolor("white")
        turtle.hideturtle()

    def forward(self, distance: float):
        self.turtle.forward(distance)

    def backward(self, distance: float):
        self.turtle.backward(distance)

    def left(self, angle: float):
        self.turtle.left(angle)

    def right(self, angle: float):
        self.turtle.right(angle)

    def goto(self, x: float, y: float):
        self.turtle.goto(x, y)

    def penup(self):
        self.turtle.penup()

    def pendown(self):
        self.turtle.pendown()

    def finish(self):
        self.turtle.end_fill()
        turtle.done()