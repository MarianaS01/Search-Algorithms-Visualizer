import pygame
import os
from sys import exit
from dimensions import *
from colors import *
from grid import *
from button import Button, Text
from menu import *
from dijkstra_algorithm import DijkstraAlgorithm
from a_star import AStar

# intialize pygame
pygame.init()

# change logo
path = os.path.abspath('assets/logo2.png')
logo_img = pygame.image.load(path)
pygame.display.set_icon(logo_img)

window = pygame.display.set_mode(WINDOW_DIMS)
pygame.display.set_caption("Search Algorithms Visualizer")

clock = pygame.time.Clock()

set_origin_button = Button((BUTTONS_POS_X, BUTTONS_POS_Y), BUTTON_SIZE)
set_origin_button.set_text("SET ORIGIN", 15, BLACK)

set_goal_button = Button((X_SECOND_COL, BUTTONS_POS_Y), BUTTON_SIZE)
set_goal_button.set_text("SET GOAL", 15, BLACK)

block_unblock_button = Button((BUTTONS_POS_X, Y_SECOND_ROW), (BUTTON_SIZE))
block_unblock_button.set_text("BLOCK/UNBLOCK CELLS", 10, WHITE)

low_speed_button = Button((X_SECOND_COL, Y_SECOND_ROW), LITTLE_BUTTON_SIZE)
pos_text = (low_speed_button.top_rect.midright[0], low_speed_button.top_rect.midright[1]-23)
speed_text_for_button = Text(pos_text, (BUTTON_WIDTH//2, BUTTON_HEIGHT))
speed_text_for_button.set_text("SPEED", 15, BLACK)
pos_speed_button = (speed_text_for_button.top_rect.midright[0], Y_SECOND_ROW)
high_speed_button = Button((pos_speed_button), LITTLE_BUTTON_SIZE)

pos_speed = (X_SECOND_COL, WIN_HEIGHT-45)
speed_text = Text(pos_speed, BUTTON_SIZE)

clean_grid_button = Button((X_SECOND_COL, Y_SECOND_ROW+NEW_ROW), BUTTON_SIZE)
clean_grid_button.set_text("CLEAN GRID", 15, BLACK)

delete_path_button = Button((BUTTONS_POS_X, Y_SECOND_ROW+NEW_ROW), BUTTON_SIZE)
delete_path_button.set_text("DELETE PATH", 15, BLACK)

# Menu
algorithms_list = ['dijkstra', 'A*']
heuristics_list = ['Manhattan distance', 'Euclidian distance', 'Chebyshev distance']

select_algorithm_button = Button((BUTTONS_POS_X, Y_SECOND_ROW+2*NEW_ROW), BUTTON_SIZE)
select_algorithm_button.set_text("SELECT ALGORITHM", 12, BLACK)
select_algorithm_button_pos = select_algorithm_button.top_rect.bottomleft

pos_menu = (select_algorithm_button_pos[0], select_algorithm_button_pos[1]+10)
menu = Menu(algorithms_list, pos_menu)

a_star_button = menu.get_button_by_text('A*')
a_star_button_pos = a_star_button.top_rect.topright

pos_submenu = (a_star_button_pos[0]+10, a_star_button_pos[1])
sub_menu = Menu(heuristics_list, pos_submenu, text_size=10)

start_button = Button((X_SECOND_COL, Y_SECOND_ROW+2*NEW_ROW), BUTTON_SIZE)
start_button.set_text("START SEARCH", 15, BLACK)

description = DescriptionBar()
grid = Grid(NUM_CELLS_ROW, NUM_CELLS_COL)
    
current_color = BLACK
delay = 100
draw_menu = False
draw_submenu = False
algorithm = None
algo = None
heuristic = None
heu = None

result_message = Text(RESMESSAGE_POS, BUTTON_SIZE)
message = None

while True:
    # process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # fill the cells
            if block_unblock_button.check_click():
                current_color = BLACK

            if set_origin_button.check_click():
                current_color = BLUE

            if set_goal_button.check_click():
                current_color = RED

            grid.fill_grid(current_color)
            
            if low_speed_button.check_click():  
                if delay < 150:
                    delay += 10
            
            if high_speed_button.check_click():
                if delay > 0:
                    delay -= 10
                
            if select_algorithm_button.check_click():
                if draw_menu:                                      
                    draw_menu = False                    
                else:
                    draw_menu = True

            if a_star_button.check_click():
                if draw_submenu:                    
                    draw_submenu = False
                else:
                    draw_submenu = True            

            algo = menu.get_algorithm()
            if algo != None:
                algorithm = algo
                if algo != a_star_button.get_text():
                    draw_menu = False

            if algorithm != 'dijkstra':
                heu = sub_menu.get_algorithm()
                if heu != None:
                    heuristic = heu
                    draw_menu = False
                    draw_submenu = False
            else:
                heuristic = None

            if grid.origin != None and grid.goal != None and message != None:
                message = None     

            if start_button.check_click():           
                if algorithm == 'dijkstra':
                    dijkstra = DijkstraAlgorithm(grid, window, delay)
                    message = dijkstra.search()
                if algorithm == 'A*':
                    a_star = AStar(grid, window, delay)
                    message = a_star.search(heuristic)

            if clean_grid_button.check_click():
                grid.clean_grid()
                # After cleaning the grid there are no errors
                message = None

            if delete_path_button.check_click():
                grid.delete_path()
            

    window.fill(GREY)
    grid.draw_grid(window)

    set_origin_button.draw_button(BLUE, window)
    set_goal_button.draw_button(RED, window)
    block_unblock_button.draw_button(BLACK, window)
    
    low_speed_button.draw_button(YELLOW, window, border_radius=5)
    low_speed_button.draw_figure('triangle_upside_down', 18, BLACK, window)
    speed_text_for_button.show_text(window)
    high_speed_button.draw_button(YELLOW, window, border_radius=5)
    high_speed_button.draw_figure('triangle', 18, BLACK, window)
    
    speed_text.set_text(f"SPEED:{150-delay}", 15, BLACK)
    speed_text.show_text(window)

    select_algorithm_button.draw_button(ORANGE, window, border_radius=10, with_animation=True)
    if draw_menu:
        menu.display_menu(window)

    if draw_submenu:
        sub_menu.display_menu(window)

    clean_grid_button.draw_button(WHITE, window)
    delete_path_button.draw_button(GAINSBORO, window)
    start_button.draw_button(GREEN, window)
    if algorithm != None:
        description.show_description(algorithm, heuristic, window)

    # PATH NOT FOUND / NO ORIGIN OR GOAL
    if message != None:
        result_message.set_text(message, text_size=20, text_color=RED)
        result_message.show_text(window)

    pygame.display.update()
    clock.tick(60)
