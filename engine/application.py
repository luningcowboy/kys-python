from __future__ import absolute_import
import sys

import pygame
import OpenGL.GL as gl

from imgui.integrations.pygame import PygameRenderer
import imgui

class Application(object):
    def __init__(self):
        pass
    def loadConf(self):
        pass
    def init(self):
        pygame.init()
        size = 800, 600
        pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
        imgui.create_context()
        self.impl = PygameRenderer()
        self.io = imgui.get_io()
        self.io.display_size = size
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.impl.process_event(event)
            imgui.new_frame()
            # render game elements
            # render gui
            gl.glClearColor(1, 1, 1, 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            imgui.render()
            self.impl.render(imgui.get_draw_data())
            pygame.display.flip()
