from math import cos, tan, pi
import pygame
from colors import *

class Text(object):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.text_rect = None
        self.top_rect = pygame.Rect(self.pos, self.size)        

    def set_text(self, text, text_size, text_color):
        self.text = text
        self.font = pygame.font.SysFont('dejavusansmono', text_size)
        self.button_text = self.font.render(self.text, True, text_color)
        self.text_rect = self.button_text.get_rect(center=self.top_rect.center)

    def show_text(self, window):
        window.blit(self.button_text, self.text_rect)

    def get_text(self):
        return self.text

class Button(Text):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.elevation = 5

    def draw_figure(self, name, size, color, window):
        center = self.top_rect.center
        
        if name == "triangle":
            angle_rad = 60*pi / 180
            bisec_angle_rad = (angle_rad/2)*pi / 180
            x = size // (2 * cos(bisec_angle_rad))
            H = int(0.5*size*tan(angle_rad))
            A = (center[0], center[1]-x)
            B = (A[0]-size//2, A[1]+H)
            C = (B[0]+size, B[1])

            vertices = (A, B, C)                
            pygame.draw.polygon(window, color, vertices)
        
        if name == "triangle_upside_down":
            angle_rad = 60*pi / 180
            bisec_angle_rad = (angle_rad/2)*pi / 180
            x = size // (2 * cos(bisec_angle_rad))
            H = int(0.5*size*tan(angle_rad))
            A = (center[0], center[1]+(H-x))
            B = (A[0]-size//2, A[1]-H)
            C = (B[0]+size, B[1])

            vertices = (A, B, C)                
            pygame.draw.polygon(window, color, vertices)

    def draw_button(self, color, window, border_radius=10, with_animation=True, back_color=SLATEGREY):
        self.bottom_color = back_color 

        # animation
        if with_animation:
            self.bottom_rect = pygame.Rect(self.pos, (self.size[0], self.elevation))
            self.original_y_pos = self.pos[1]
            
            self.top_rect.y = self.original_y_pos - self.elevation
            if self.text_rect != None:
                self.text_rect.center = self.top_rect.center
            self.bottom_rect.midtop = self.top_rect.midtop
            self.bottom_rect.height = self.top_rect.height + self.elevation

            pygame.draw.rect(window, self.bottom_color, self.bottom_rect, border_radius=border_radius)
        
        pygame.draw.rect(window, color, self.top_rect, border_radius=border_radius)
        
        if self.text_rect != None:
            window.blit(self.button_text, self.text_rect)
        self.check_click()

    def check_click(self):
        self.is_pressed = False
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            # check right click
            if pygame.mouse.get_pressed()[0]: 
                self.elevation = 0
                self.is_pressed = True

            else:
                self.elevation = 5
        return self.is_pressed
