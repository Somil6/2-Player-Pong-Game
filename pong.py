import pygame
from sys import exit
import random

# Initialize window
window_width=800
window_height=600
pygame.init()
window = pygame.display.set_mode((window_width,window_height))

# Set caption
pygame.display.set_caption("PONG GAME")

# Control frame rate
clock = pygame.time.Clock() 

# Paddle object
paddle_width =25
paddle_height=120
paddle1 = pygame.Rect((775, 240 , paddle_width ,paddle_height))
paddle2 = pygame.Rect((0 , 240, paddle_width , paddle_height))

# Ball object
ball_width =25
ball_height=25
ball_start_x = (window_width-ball_width)//2 
ball_start_y = (window_height-ball_height)//2
ball = pygame.Rect((ball_start_x , ball_start_y, ball_width, ball_height))
Choice=[6,-6]
ball_x_change = random.choice(Choice)
ball_y_change =-6

# Draw objects in game window
def draw():
  window.fill((0,0,0))
  pygame.draw.rect(window, (255,255,255), paddle1)
  pygame.draw.rect(window, (255,255,255), paddle2)
  pygame.draw.rect(window, (255,255,255), ball)
  pygame.draw.line(window, (255,255,255),(394,0),(394,window_height))

# Score
player1_score = 0
player2_score = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)

# Coordinates of players' scores
player1_score_x  = 360
player1_score_y  = 34
player2_score_x  = 410
player2_score_y = 34

# Check if a player won, display the win message, and prompt for restart
def win_message(scoreValue, message):
    global player1_score
    global player2_score
  
    if scoreValue >=10:     
       player1Wins = font1.render(message, True , (255,0,0))
       window.blit(player1Wins,(300,320))
       pygame.display.flip()
       pygame.time.delay(1000)

       restartGame = font1.render("PRESS SPACEBAR TO PLAY AGAIN",True,(0,255,0))
       window.blit(restartGame,(135,350))

       # Clear score
       player1_score=0
       player2_score=0
       pygame.display.flip()
       
       #Loop to display restart message until spacebar key is pressed
       running = True
       while running:
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                exit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   running = False
                  
# Display score on screen
def show_score(a , b , c , d):
    global player1_score
    global player2_score
  
    score1 = font1.render(str(player1_score), True, (255, 255, 255))
    window.blit(score1, (a, b))
    score2 = font1.render(str(player2_score), True, (255, 255, 255))
    window.blit(score2, (c, d))
   
    win_message(player1_score,"PLAYER 1 WINS")
    win_message(player2_score, "PLAYER 2 WINS")

# Function to reset ball at centre after a point is scored
def reset_ball():
   global ball_x_change
   global ball_y_change
   ball_x_change = random.choice(Choice)
   ball_y_change = random.choice([6, -6])
   ball.x =ball_start_x
   ball.y =ball_start_y
  
# Gameloop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  
  # Get all currently pressed keys
  keys = pygame.key.get_pressed()
  
  # Movement of paddles according to keys pressed
  if keys[pygame.K_UP]: 
    paddle1.y +=-5
  if keys[pygame.K_DOWN]:
    paddle1.y +=5
  if keys[pygame.K_w]:
    paddle2.y +=-5
  if keys[pygame.K_s]:
    paddle2.y +=5

  # Boundaries of paddle 1
  if paddle1.y>=480 :
     paddle1.y = 480
  if paddle1.y<=0 :
     paddle1.y = 0

  # Boundaries of paddle 2
  if paddle2.y>=480 :
     paddle2.y = 480
  if paddle2.y<=0 :
     paddle2.y = 0
    
  # Bounce the ball off top and bottom walls
  if ball.y >=575:
     ball_y_change =-6
  if ball.y <=0:
     ball_y_change =6
  
  # Player scores a point if the ball crosses the paddle without collision
  if ball.x >= 775: 
     player1_score+=1
     reset_ball()
  if ball.x<=0:
     player2_score+=1
     reset_ball()
     
  # Collision detection
  if paddle1.colliderect(ball):
     ball_x_change =-6 # Reverse ball direction on paddle hit
  if paddle2.colliderect(ball):
     ball_x_change = 6
  
  # Reflect all changes in position of ball
  ball.x += ball_x_change
  ball.y += ball_y_change
  
  # Draw paddles, ball and centre line
  draw() 
  show_score(player1_score_x , player1_score_y , player2_score_x , player1_score_y)
  pygame.display.update()
  clock.tick(60)