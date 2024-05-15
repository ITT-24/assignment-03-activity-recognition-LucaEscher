# this program visualizes activities with pyglet

from activity_visualizer import ActivityVisualizer
import os
import pyglet
from pyglet.gl import glClearColor

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
glClearColor (255, 255, 255, 1.0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        os._exit(0)
    if symbol == pyglet.window.key.SPACE:
        global visualizer
        visualizer.visualizer_state = 1


@window.event
def on_draw():
    window.clear()
    visualizer.update()


if __name__ == '__main__':
    global visualizer
    visualizer = ActivityVisualizer(WINDOW_WIDTH, WINDOW_HEIGHT)
    visualizer.run()