import pygame
import random

pygame.init()

#Screen dimensions, color and font
bg = (65, 140, 11)
snake = (255, 204, 0)
food = (242, 29, 29)
points = (255, 255, 255)

dim = (600, 600)

screen = pygame.display.set_mode((dim))
pygame.display.set_caption('Snake')

screen.fill(bg)

font = pygame.font.SysFont("Comic Sans MS", 30)

#Snake initial position and size
x = 300
y = 300
d = 20

listSnake = [[x, y]]

#Movement direction
dx = 0
dy = 0

#Food position
xFood = round(random.randrange(0, 600 - d) / 20) * 20
yFood = round(random.randrange(0, 600 - d) / 20) * 20

#Defining 'clock' to update
clock = pygame.time.Clock()

#'Drawing' snake
def drawSnake(listSnake):
    screen.fill(bg)
    for unit in listSnake:
      pygame.draw.rect(screen, snake, [unit[0], unit[1], d, d])

#Snake movement
def moveSnake(dx, dy, listSnake):

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        dx = -d    
        dy = 0
      elif event.key == pygame.K_RIGHT:
        dx = d
        dy = 0 
      elif event.key == pygame.K_UP:
        dx = 0
        dy = -d 
      elif event.key == pygame.K_DOWN:
        dx = 0
        dy = d 

  newX = listSnake[-1][0] + dx
  newY = listSnake[-1][1] + dy

  listSnake.append([newX, newY])

  del listSnake[0]

  return dx, dy, listSnake

#Food position and 'drawing'
def verifyFood(dx, dy, xFood, yFood, listSnake):
  head = listSnake[-1]
  newX = head[0] + dx
  newY = head[1] + dy

  if head[0] == xFood and head[1] == yFood:
    listSnake.append([newX, newY])
    xFood = round(random.randrange(0, 600 - d) / 20) * 20
    yFood = round(random.randrange(0, 600 - d) / 20) * 20

  pygame.draw.rect(screen, food, [xFood, yFood, d, d])
  return xFood, yFood, listSnake

#Verifies if the snake has left the screen boundary. If so, the game ends
def verifyWall(listSnake):
  head = listSnake[-1]
  x = head[0]
  y = head[1]

  if x not in range(600) or y not in range(600):
    raise Exception

#Verifies if the snake has bitten itself. If so, the game ends
def verifySnakeBite(listSnake):
  head = listSnake[-1]
  body = listSnake.copy()

  del body[-1]

  for x, y in body:
    if x == head[0] and y == head[1]:
      raise Exception

#Score
def score(listSnake):
  pts = str(len(listSnake))
  score = font.render('Score: ' + pts, True, points)
  screen.blit(score, [25, 25])

while True: 
    pygame.display.update()
    drawSnake(listSnake)
    dx, dy, listSnake = moveSnake(dx, dy, listSnake)
    xFood, yFood, listSnake = verifyFood(dx, dy, xFood, yFood, listSnake)
    verifyWall(listSnake)
    verifySnakeBite(listSnake)
    score(listSnake)
    
    print(listSnake)

    #Snake speed
    clock.tick(10)