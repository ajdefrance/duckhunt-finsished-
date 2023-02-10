# PyGame Tutorial -- Mike Webb
# V 3.0 -- 1/9/23

import pygame, sys, mixer
import os

# How to add music to application
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('Assets', 'music.mp3'))
pygame.mixer.music.play()

pygame.init()   # this initiates the application

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Pygame Tutorial')
surface = pygame.Surface((100, 100))
surface.fill('green')
clock = pygame.time.Clock()
car = pygame.image.load(os.path.join('Assets', 'shipu.png'))
pygame.display.set_icon(car)

# Load rocket and space background images
rocket1 = pygame.image.load(os.path.join('Assets', 'rocket.png'))
rocket = pygame.transform.scale(rocket1, (25, 25))
bg = pygame.image.load(os.path.join('Assets', 'bgspace.jpg'))

x_pos = 20
y_pos = 20
step = 3
angle = 0
move_right = False
move_left = False
move_down = False
move_up = False

while True:
   screen.blit(bg, (0, 0))
   screen.blit(surface, (250, 200))

   # Update box position and draw box with rocket image
   if move_left:
       x_pos -= step
       angle = 90
   if move_right:
       x_pos += step
       angle = 270
   if move_up:
       y_pos -= step
       angle = 0
   if move_down:
       y_pos += step
       angle = 180

   # set bounds so that the image can't leave the screen bounds
   if x_pos > 250 and x_pos < 350 and y_pos > 200 and y_pos < 300:

       # Set the square's position to just outside the surface of the surface and place it on opposite side of it
       if move_left:
           x_pos = 249
       elif move_right:
           x_pos = 351
       elif move_up:
           y_pos = 199
       elif move_down:
           y_pos = 301
   if x_pos < 0:
       x_pos = 0
   if x_pos > 580:
       x_pos = 580
   if y_pos < 0:
       y_pos = 0
   if y_pos > 480:
       y_pos = 480


   # Drawing the rect & attaching the image to it
   box = pygame.draw.rect(screen, 'black', (x_pos, y_pos, 20, 20), 1)
   screen.blit(rocket, (x_pos, y_pos))

   if move_left and x_pos > 0:  # Check if box is at the left edge of the screen
       x_pos -= step
       angle = 90
   if move_right and x_pos < 580:  # Check if box is at the right edge of the screen
       x_pos += step
       angle = 270
   if move_up and y_pos > 0:  # Check if box is at the top edge of the screen
       y_pos -= step
       angle = 0
   if move_down and y_pos < 480:  # Check if box is at the bottom edge of the screen
       y_pos += step
       angle = 180

   # Rotate rocket image in the direction it is headed... made is a perfect square
   rotated_rocket = pygame.transform.rotate(rocket, angle)
   rotated_rect = rotated_rocket.get_rect(center=rocket.get_rect(topleft=(x_pos, y_pos)).center)

   # Blit the rotated rocket image on screen with the direction... rotated rocket
   screen.blit(rotated_rocket, rotated_rect)

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       # Lines below process the events of the keyboard
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
               move_right = True
           if event.key == pygame.K_LEFT:
               move_left = True
           if event.key == pygame.K_DOWN:
               move_down = True
           if event.key == pygame.K_UP:
               move_up = True
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT:
               move_right = False
           if event.key == pygame.K_LEFT:
               move_left = False
           if event.key == pygame.K_DOWN:
               move_down = False
           if event.key == pygame.K_UP:
               move_up = False

   pygame.display.update()
   clock.tick(60)

