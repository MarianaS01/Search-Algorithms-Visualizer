import pygame
from colors import *
from dimensions import *
from button import *

class Square(object):
    def __init__(self, pos):
        SIDE_LEN = 15
        self.square_rect = pygame.Rect(pos, (SIDE_LEN, SIDE_LEN))

    def set_text(self, text, text_size, text_color):
        self.font = pygame.font.SysFont('dejavusansmono', text_size)
        self.text = self.font.render(text, True, text_color)
        midleft = (self.square_rect.midright[0]+10, self.square_rect.midright[1])
        self.text_rect = self.text.get_rect(midleft=midleft)

    def draw(self, color, window):
        pygame.draw.rect(window, color, self.square_rect)
        window.blit(self.text, self.text_rect)

class DescriptionBar(object):
    def __init__(self):
        self.dijkstra = self.a_star = {
            'To visit': ORANGE,
            'Visited': YELLOW,
            'Add neighbour': KHAKI,
            'Replace': PURPLE,
            'Path': GREEN
        }

    def show_description(self, algorithm_name, heuristic, window):
        SPACE = 25
        if algorithm_name == 'dijkstra':
            algorithm = self.dijkstra
        if algorithm_name == 'A*':
            algorithm = self.a_star
        for phase in algorithm.keys():
            phase_sqr = Square((SPACE, WIN_HEIGHT-33))
            phase_sqr.set_text(phase, 12, BLACK)
            phase_sqr.draw(algorithm[phase], window)
            SPACE = phase_sqr.text_rect.midright[0] + 25
        
        pos_current_algo_text = (SPACE+3.5*BUTTONS_POS_Y, WIN_HEIGHT-45)
        current_algorithm_text = Text(pos_current_algo_text, BUTTON_SIZE)
        if heuristic != None:
           current_algorithm_text.set_text(f'Algorithm: {algorithm_name}, Heuristic: {heuristic}', 15, BLACK)
        else:
            current_algorithm_text.set_text(f'Algorithm: {algorithm_name}', 15, BLACK)
        current_algorithm_text.show_text(window)

class Menu(object):
    def __init__(self, algorithms_list, pos, text_size=12):
        self.algorithms_list = algorithms_list
        self.buttons_list = []

        for algorithm in self.algorithms_list:
            button = Button(pos, OPTION_BUTTON_SIZE)
            button.set_text(algorithm, text_size, BLACK)
            pos = (pos[0], pos[1]+BUTTON_HEIGHT)
            
            self.buttons_list.append(button)

    def display_menu(self, window):
        for button in self.buttons_list:
            button.draw_button(ORANGE, window, border_radius=0, with_animation=True, back_color=ORANGE)
        
        pygame.display.update([button.top_rect for button in self.buttons_list])

    def get_algorithm(self):
        for button in self.buttons_list:
            if button.check_click():
                return button.get_text()
            else:
                continue

    def get_button_by_text(self, text_in_button):
        for button in self.buttons_list:
            if button.get_text() == text_in_button:
                return button