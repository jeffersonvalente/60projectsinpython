import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init
random.seed()

#global constants

SPEED = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE #mantem o tamanho da fruta = ao da cobra
SEPARATION = 10 #separação entre dois pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1, "DOWN":2, "LEFT":3, "RIGHT":4}#dicionario dos botoes

#inicia a tela
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH),pygame.HWSURFACE) #hwsurface usa a memoria da placa de video ao inves da memoria ram

#Resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0) #preechimento do fundo de preto
black = pygame.Color(0,0,0)

#tempo de jogo
gameClock= pygame.time.Clock()

def checkColission(posA, As, posB, Bs):  #As é o tamanho de A (Asize), Bs é o tamanho de B (Bsize)
    if(posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0): #Isto será verificado quando alguma parte da cobra estiver de um lado e alguma outra parte estiver do lado oposto.
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0):
        snake.y - SCREEN_HEIGHT - SNAKE_SIZE
    
#maça

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y 
        self.state = state 
        self.color = pygame.color.Color("orange")

    def draw(self,screen):
        pygame.drawn.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)

class segment:     #inicia o movimento apertando UP
    self.x = x
    self.y = y 
    self.direction = KEY["UP"]
    self.color = "white"
    
class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"] 
        blackBox = segment(self.x, self.y + SEPARATION)
        blackBox.direction = KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)
    
    def move(self):
        last_element = len(self.stack) - 1
        while(last_element != 0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element - 1].x
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -=1
        if(len(self,stack) < 2):
            last_segment = self
        else:
            last_segment = self.stack.pop(last_element)
        last_segment.direction = self.stack[0].direction
        if(self.stack[0].direction == KEY["UP"]):
            last_segment.y = self.stack[0].y - (SPEED * FPS)
        elif(self.stack[0].direction == KEY["DOWN"]):
            last_segment.y = self.stack[0].y + (SPEED * FPS)
        elif(self.stack[0].direction == KEY["UP"]):
            last_segment.y = self.stack[0].y - (SPEED * FPS)
        elif(self.stack[0].direction == KEY["LEFT"]):
            last_segment.x = self.stack[0].x - (SPEED * FPS)
        elif(self.stack[0].direction == KEY["RIGHT"]):
            last_segment.x = self.stack[0].x + (SPEED * FPS)
        self.stack.insert(0,last_segment)
        
    def getHead(self):#saber onde ta a cabeça
        return(self.stack[0])#sempre vai ser o index 0
    
    def grow(self): #faz a cobra crescer XD
        last_element = len(self.stack) -1
        self.stack[last_element].direction = self.stack[last_element].direction
        if(self.stack[last_element].direction == KEY["UP"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y - SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y - SEPARATION)
            
        elif(self.stack[last_element].direction == KEY["DOWN"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y + SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y + SEPARATION)
             
        elif(self.stack[last_element].direction == KEY["LEFT"]):
            newSegment = segment(self.stack[last_element].x, - SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segment(newSegment.x, - SEPARATION, newSegment.y )
            
        elif(self.stack[last_element].direction == KEY["RIGHT"]):
            newSegment = segment(self.stack[last_element].x, + SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segment(newSegment.x, + SEPARATION, newSegment.y )
            
        blackBox.color = "NULL"       
        self.stack.append(newSegment)
        self.stack.append(blackBox)
    
    def iterateSegments(self,delta):
        pass
    
    def setDirection(self,direction):
        if(self.direction == KEY["RIGHT"] and direction == KEY["LEFT"] or self.direction == KEY["LEFT"] and
           direction == KEY["RIGHT"]):
            pass
        elif(self.direction == KEY["UP"] and direction == KEY["DOWN"] or self.direction == KEY["UP"] and
           direction == KEY["DOWN"]):
            pass
        else:
            self.direction = direction
              
#teclas
def getkey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            #sair do game
            if event.key == pygame.K_ESCAPE:
                return "exit"
            #continuar jogando
            elif event.key == pygame.K_y:
                return "yes"
            #não continuar jogando
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

            
def endGame():
    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Pla Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

    pygame.display.flip()
    pygame.display.update()
    
    mKey = getkey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getkey()
        gameClock.tick(FPS)
    sys.exit(0)
    
def drawnScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH - 45,14))
    
def drawGameTime(gameTime):
    game_time = score_font.render("Time:" , 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))
    screen.blit(game_time,(30,10))
    screen.blit(game_time_numb,(105,14))
    
def exitScreen():
    pass

def main():
    print("inicializou")