# PyGame Tutorial
# V 3.0 -- 1/9/23

import pygame, sys, mixer
import os


# How to add music to application
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('Assets', 'star-war-111422.mp3'))
pygame.mixer.music.play()

pygame.init()   # this initiates the application
ds = pygame.image.load(os.path.join('Assets',"deathstar.png"))
ds = pygame.transform.scale(ds, [75,75])
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Malicious Program')
surface = pygame.Surface((100, 100))
surface2 = pygame.Surface((100, 100))
clock = pygame.time.Clock()
car = pygame.image.load(os.path.join('Assets', 'shipu.png'))
pygame.display.set_icon(car)

# Load rocket and space background images
rocket1 = pygame.image.load(os.path.join('Assets', 'xwing.png'))
rocket = pygame.transform.scale(rocket1, (25, 25))
bg = pygame.image.load(os.path.join('Assets', 'stars.png'))
bigrock = pygame.image.load(os.path.join('Assets', 'big_rock.png'))
bigrock1 = pygame.transform.scale(bigrock, (50, 50))
ship1 = pygame.image.load(os.path.join('Assets', 'tie.png'))
ship1 = pygame.transform.scale(ship1, (25, 25))
White = (255, 255, 255)
x_pos = 20
y_pos = 20
step = 3
step2 = 6
angle = 0
angle2 = 0
rock_y = 0
rock_x = 0
move_right = False
move_left = False
move_down = False
move_up = False
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 400
Y = 400
lives = 10
lives2 = 10
# New variables for second rect
x_pos2 = 550
y_pos2 = 450
move_up2 = False
move_down2 = False
move_left2 = False
move_right2 = False
rock_right = True
rock_bottom = True
display_surface = pygame.display.set_mode((600, 500))
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Star Game', True, green)
textRect = text.get_rect()
textRect.center = (X // 1.3, Y // 9)

surface.blit(ds, (x_pos, y_pos))
while True:
   screen.blit(bg, (0, 0))
   screen.blit(surface, (250, 200))
   display_surface.blit(text, textRect)
   if rock_right == True:
    rock_x += 2
   else:
    rock_x -= 2
   if rock_bottom == True:
    rock_y += 2
   else:
    rock_y -= 2
   if rock_x <= 0:
    rock_right = True
   if rock_x >= 550:
    rock_right=False
   if rock_y <= 0:
    rock_bottom=True
    
   if rock_y >= 450:
    rock_bottom=False



   screen.blit(bigrock1, (rock_x, rock_y))


   # Update box position and draw box with rocket image.............
   if move_left:
       x_pos -= step
       angle = 270
            
   if move_right:
       x_pos += step
       angle = 90
       
   if move_up:
       y_pos -= step
       angle = 0
      
   if move_down:
       y_pos += step
       angle = 180
      # Update position of second rect

   if move_left2:
       x_pos2 -= step2
       angle2 = 180
   if move_right2:
       x_pos2 += step2
       angle2 = 0
       
   if move_up2:
       y_pos2 -= step2
       angle2 = 90
       
   if move_down2:
       y_pos2 += step2
       angle2 = 270
       
   if x_pos2 > 250 and x_pos2 < 350 and y_pos2 > 200 and y_pos2 < 300:
   

       # Set the square's position to just outside the surface of the surface and place it on opposite side of it
       if move_left2:
           x_pos2 = 249
       elif move_right2:
           x_pos2 = 351
       elif move_up2:
           y_pos2 = 199
       elif move_down2:
           y_pos2 = 301  
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
   if x_pos2 < 0:
       x_pos2 = 0
   if x_pos2 > 580:
       x_pos2 = 580
   if y_pos2 < 0:
       y_pos2 = 0
   if y_pos2 > 480:
       y_pos2 = 480
 
   # Drawing the rect & attaching the image to it
   box = pygame.draw.rect(screen, 'black', (x_pos, y_pos, 20, 20), 1)
   box2 = pygame.draw.rect(screen, 'black', (x_pos2, y_pos2, 20, 20), 1)
  
   

   if move_left and x_pos > 0:  # Check if box is at the left edge of the screen
       x_pos -= step
       angle = 270
   if move_right and x_pos < 580:  # Check if box is at the right edge of the screen
       x_pos += step
       angle = 90
     
   if move_up and y_pos > 0:  # Check if box is at the top edge of the screen
       y_pos -= step
       angle = 180
       
   if move_down and y_pos < 480:  # Check if box is at the bottom edge of the screen
       y_pos += step
       angle = 0 
   
    
           
       # Set the second square's position to just outside the surface of the surface and place it on opposite side of it
       if move_left2:
           x_pos2 = 249
           angle2 = 180
       elif move_right2:
           x_pos2 = 351
           angle2 = 0
       elif move_up2:
          y_pos2 = 199
          angle2 = 270
       elif move_down2:
           y_pos2 = 301
           angle2 = 90
   if x_pos2 < 0:
       x_pos2 = 0
   if x_pos2 > 580:
       x_pos2 = 580
   if y_pos2 < 0:
       y_pos2 = 0
   if y_pos2 > 480:
       y_pos2 = 480
   if x_pos == rock_x or x_pos ==rock_x and y_pos == rock_y or y_pos == rock_y:
        lives -=1
        print(lives)
   if x_pos2 == rock_x or x_pos2 ==rock_x and y_pos2 == rock_y or y_pos2 == rock_y:
        lives2 -=1
        print(lives2)
# Rotate rocket image in the direction it is headed... made is a perfect square
   rotated_rocket = pygame.transform.rotate(rocket, angle)
   rotated_rect = rotated_rocket.get_rect(center=rocket.get_rect(topleft=(x_pos, y_pos)).center)
   rotated_rocket2 = pygame.transform.rotate(ship1, angle2)
   rotated_rect2 = rotated_rocket2.get_rect(center=ship1.get_rect(topleft=(x_pos2, y_pos2)).center)

   screen.blit(rotated_rocket, rotated_rect)
   screen.blit(rotated_rocket2, rotated_rect2)


   for event in pygame.event.get():
       if event.type == pygame.QUIT or lives2 == 0 or lives == 0:
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
           if event.key == pygame.K_d:
               move_right2 = True
           if event.key == pygame.K_a:
               move_left2 = True
           if event.key == pygame.K_w:
               move_up2 = True
           if event.key == pygame.K_s:
               move_down2 = True
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT:
               move_right = False
           if event.key == pygame.K_LEFT:
               move_left = False
           if event.key == pygame.K_DOWN:
               move_down = False
           if event.key == pygame.K_UP:
               move_up = False
           if event.key == pygame.K_d:
               move_right2 = False
           if event.key == pygame.K_a:
               move_left2 = False
           if event.key == pygame.K_w:
               move_up2 = False
           if event.key == pygame.K_s:
               move_down2 = False
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       # Lines below process the events of the keyboard
   pygame.display.update()
   clock.tick(60)

