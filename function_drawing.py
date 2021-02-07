from p5 import *

window_height = 640
window_width = 360


def mum_setup():
    size(window_width, window_height)
    stroke(255)


def mum_draw():
    background(0)

    for i in range(10):
        star(i * 100, i * 50)


def star(position_x, position_y):
    push_matrix()
    translate(position_x, position_y)
    triangle(0, 0, 100, 100, 0, 100)
    pop_matrix()


run(sketch_setup=mum_setup, sketch_draw=mum_draw)
