import sys
import pygame
import random

pygame.init()

width = 800
height = 600
size = (width, height)
black = (0,0,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rat Click Game")

Rat = pygame.image.load("Rat.png")

iterator = 0
numofRats = 5
startX = []
startY = []
speed = []

while iterator < numofRats:
  startX.append(random.randint(0, width - Rat.get_width() + 1))
  startY.append(0 - random.randint(Rat.get_height(), Rat.get_height() * 2))
  speed.append(0.5)
  iterator += 1

  # -------------------------
# POWER-UP SETUP
# -------------------------
powerup = pygame.Surface((60, 60))
powerup.fill((0, 0, 255))  # Blue square
powerup_x = width - 120
powerup_y = 40
powerup_active = True

def increase_speed():
    for i in range(numofRats):
        speed[i] += 1.8 #custom speed increase value
# -------------------------

replayscreen = False
#Set up game over stuff
bigfont = pygame.font.SysFont(None, 200)
playagaintext = bigfont.render("Play Again?", True, (0,200,0))
pax = width/2 - playagaintext.get_rect().width/2

smallfont = pygame.font.SysFont(None, 100)
yestext = smallfont.render("YES", True, (0, 200, 0))
yesx = width/4 - yestext.get_rect().width/2
notext = smallfont.render("NO", True, (0,200,0))
nox = width - width/4 - yestext.get_rect().width/2

#Game Loop

gameover = False

while gameover == False:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameover = True

  #Clicking on the Rats
  if pygame.mouse.get_pressed()[0]:
    coords = pygame.mouse.get_pos()
    if replayscreen == False:
      iterator = 0
      while iterator < numofRats:
        if coords[0] >= startX[iterator] and coords[0] <= startX[iterator] + Rat.get_width() and coords[1] > startY[iterator] and coords[1] < startY[iterator] + Rat.get_height():
          startX[iterator] =  random.randint(0, width - Rat.get_width() + 1)
          startY[iterator] = 0 - random.randint(Rat.get_height(), Rat.get_height() * 2)
          speed[iterator] = 0.5
          break
        iterator += 1
    else:
      if coords[0] > yesx and coords[0] < yesx + yestext.get_rect().width and coords[1] > 450 and coords[1] < 450 + yestext.get_rect().height:
        iterator = 0
        while iterator < numofRats:
          startX[iterator] =  random.randint(0, width - Rat.get_width() + 1)
          startY[iterator] = 0 - random.randint(Rat.get_height(), Rat.get_height() * 2)
          speed[iterator] = 0.5
          iterator +=1
        replayscreen = False

      if coords[0] > nox and coords[0] < nox + notext.get_rect().width and coords[1] > 450 and coords[1] < 450 + notext.get_rect().height:
        gameover = True


  #Updating
  if replayscreen == False:
    iterator = 0
    #Game over
    while iterator < numofRats:
      if startY[iterator] + Rat.get_height() > height:
        replayscreen = True
        break
      startY[iterator] += speed[iterator]
      iterator += 1


  #Drawing

  if replayscreen == False:
    screen.fill(black)
    iterator = 0
    while iterator < numofRats:
      screen.blit(Rat, (startX[iterator], startY[iterator]))
      iterator += 1

    iterator = 0
  else:
    screen.fill((200,0,0))

    screen.blit(playagaintext, (pax, 150))
    screen.blit(yestext, (yesx, 450))
    screen.blit(notext, (nox, 450))

  pygame.display.flip()

pygame.display.quit()