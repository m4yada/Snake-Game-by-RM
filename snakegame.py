#https://www.pygame.org/docs/
#https://www.edureka.co/blog/snake-game-with-pygame/
#https://www.geeksforgeeks.org/python-display-images-with-pygame/
#https://pygame-menu.readthedocs.io/en/latest/
#https://chat.openai.com/

#Brings pygame files
import pygame
#Operation system
import os
#Pyhton package that could give you random value
import random
#Importing system
import sys
import time 
 
#Pygame screen
pygame.init()
#Screen geometry
scrn_width = 700
scrn_height = 600
screen = pygame.display.set_mode((700,600))
#Screen title
pygame.display.set_caption('Snake Game by RM')
#Load bg image
bg_img = pygame.image.load('pysnakegame\snakegamebg2.jpg')
bg_img2 = pygame.image.load('pysnakegame\snakegamebg.jpg')

#Game menu status
game_menu = False

#Font style
py_font = pygame.font.SysFont(None, 50)
py_font2 = pygame.font.SysFont(None, 55)

#Set up colors
green = ('#0d421e')
red = (225,0,0)
white = (225,225,225)
black = (0, 0, 0)

#Set up rectangles (snake, apple)
player_rect = pygame.Rect(50, 50, 50, 50)
food_rect = pygame.Rect(random.randint(0, scrn_width - 30), random.randint(0, scrn_height - 30), 30, 30)

#Divisioning width and height
x1 = scrn_width/2
y1 = scrn_height/2

x1_change = 0       
y1_change = 0

# Initial snake length
snake_length = 1
snake_segments = [{'x': x1, 'y': y1}]

#Running the game on True
running = True

#Set up clock
clock = pygame.time.Clock()

#Drawing text, font, color, surface, x, y
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)

# Font and button colors
font = pygame.font.Font(None, 36)
button_color = (102,225,102)
hover_color = ('#067529')

# Function to draw buttons
def draw_button(screen, text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, button_color, (x, y, width, height))

    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

#Function to start the game
def start_game():
    global game_state
    game_state = 'Playing'

#Function to restart game
def restart_game():
    global game_state
    game_state = 'Playing'

#Function to quit the game
def quit_game():
    sys.exit()

#Function for message
def message(msg,color):
    mesg = py_font.render(msg, True, color)
    screen.blit(mesg, [scrn_width/2, scrn_height/2])


#Main game loop
running = True
game_state = 'Menu'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    screen.fill(white)

    #Using blit to copy contect from the one surface to other
    screen.blit(bg_img, (0,0))

    #Snake, apple drawing
    pygame.draw.rect(screen, green, [x1, y1, 45, 45])
    pygame.draw.rect(screen, red, food_rect)

     # Check for collision with food
    if player_rect.colliderect(food_rect):
        food_rect.x = random.randint(0, scrn_width - 30)
        food_rect.y = random.randint(0, scrn_height - 30)

        # Increase snake length
        snake_length += 2

    # Update snake segments
    if snake_length >= 1:
        snake_segments.insert(0, {'x': x1, 'y': y1})
        if len(snake_segments) > snake_length:
            snake_segments.pop()

    # Draw snake segments
    for segment in snake_segments:
        pygame.draw.rect(screen, green, [segment['x'], segment['y'], 45, 45])

    #Check for collision with boundries
    if x1 == scrn_width or x1 == 0 or y1 == scrn_height or y1 == 0:
        # screen.fill(black)
        pygame.display.update()

        # Calculate the position to center the message
        text_surface = py_font.render('You Lost!', True, black)
        text_rect = text_surface.get_rect(center=(scrn_width / 2, scrn_height / 2))

        screen.blit(text_surface, text_rect)

        #Restart button
        restart_button = draw_button(screen, 'Restart', 250, 350, 200, 50, start_game)
        pygame.display.update()

        restart_clicked = False
        while not restart_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    restart_clicked = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.colliderect(event.pos):
                        x1 = scrn_width / 2
                        y1 = scrn_height / 2
                        x1_change = 0
                        y1_change = 0
                        restart_clicked = True
                    
        pygame.time.delay(4000)  # Delay for 4000 milliseconds (4 seconds)
        pygame.display.update()
        running = False

    #Drawing main menu(screen & buttons)
    if game_state == 'Menu':
        screen.blit(bg_img2, (-585, -250))
        draw_text("Snake game RM", py_font2, black, screen, 369, 110)

        draw_button(screen, 'Start Game', 400, 200, 200, 50, start_game)
        draw_button(screen, 'Quit', 400, 300, 200, 50, quit_game)

    #Snake speed
    clock.tick(30)

    # Update the display
    pygame.display.flip()
    #Window display 
    pygame.display.update()

pygame.quit()
quit()