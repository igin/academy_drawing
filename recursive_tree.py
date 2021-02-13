from p5 import *

window_height = 1000
window_width = 1000


def main_setup():
    size(window_width, window_height)
    stroke(255)


def main_draw():

    background(0)
    # move origin to center of window
    translate(window_width * 0.5, window_height)

    # draw a tree of depth 6
    depth = 7
    tree(depth)


angle = 0.5
rotation_left = -angle
rotation_right = angle * 0.6
scale_left = 0.6
scale_right = 0.9


def tree(depth):

    if depth == 0:
        fill(0, 255, 0)
        circle(0, 0, 20)
        return

    # draw the line
    line(0, 0, 0, -100)

    # move the origin to the end of the line
    translate(0, -100)

    # draw the left subtree
    push_matrix()
    scale(scale_left, scale_left)
    rotate_z(rotation_left - (mouse_y * 0.001))
    tree(depth - 1)
    pop_matrix()

    # draw the right subtree
    push_matrix()
    scale(scale_right, scale_right)
    rotate_z(rotation_right)
    tree(depth - 1)
    pop_matrix()


run(sketch_setup=main_setup, sketch_draw=main_draw)
