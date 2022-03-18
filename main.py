import pygame 
from backgammon.constants import WIDTH, HEIGHT
import random
from tkinter import *
import sys


FPS = 60

pygame.init()

background_image = pygame.image.load("img/background.png")
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Backgammon Game")

def main():
    run = True
    clock = pygame.time.Clock()

    display.fill((0,0,0))
    display.blit(background_image, (0,0))

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False      

        pygame.display.update()

    pygame.quit()

#Dice values and store in txt file
def roll_dice():
    value_1: random.randint(1,6)
    value_2: random.randint(1,6)
    dice1.my_dice = pygame.image.load(you_dice[value_1-1])
    dice2.my_dice = pygame.image.load(you_dice[value_1-1])
    write_in_file("{} {}".format(value_1, value_2),"txt/dice_save.txt")

def cpu_roll_dice():
    value_1: random.randint(1,6)
    value_2: random.randint(1,6)
    dice1_cpu.my_dice = pygame.image.load(cpu_dice_list[value_1-1])
    dice2_cpu.my_dice = pygame.image.load(cpu_dice_list[value_1-1])
    write_in_file("{} {}".format(value_1, value_2),"txt/cpu_dice_save.txt")

def write_in_file(content, file_name):
    file = open(file_name, "w")
    file.write(content)
    file.close()

def return_value_from_file(file_name = "txt/dice_save.txt"):
    file = open(file_name, "r")
    a = file.read().split()
    file.close()
    return (int(a[0]), int(a[-1]))

#Button images for dice rolls
inactive_dice_button = pygame.image.load("img/dice_button.png")
active_dice_button = pygame.image.load("img/active_dice_button.png")

you_dice = [
    "img/you_dice1.png"
    "img/you_dice2.png"
    "img/you_dice3.png"
    "img/you_dice4.png"
    "img/you_dice5.png"
    "img/you_dice6.png"
]

cpu_dice_list = [
    "img/cpu_dice1.png"
    "img/cpu_dice2.png"
    "img/cpu_dice3.png"
    "img/cpu_dice4.png"
    "img/cpu_dice5.png"
    "img/cpu_dice6.png" 
]

main()
exit()
