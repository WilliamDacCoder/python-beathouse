import os
import pygame
import random

def randnum(a, b):
    num = random.randint(a, b)
    return num


def numberofmembers(list):
    ammount = -1
    for e in list:
        ammount = ammount+1
    return(ammount)


pygame.init()
pygame.mixer.music.set_volume(0.5)
dir_path = os.path.dirname(os.path.realpath(__file__))
files = []
paused = False
d = dir_path+"\\mp3s"
ymod = False


def getmembernum(list,deff):
    e = -1
    for a in list:
        e = e + 1
        if a == deff:
            return(e)
def randomsong():
    ammount = numberofmembers(files)
    num = randnum(0, ammount)
    member = files[num]
    pygame.mixer.music.load(member)
    pygame.mixer.music.play()
pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    full_name = os.path.basename(full_path)
    files.append(full_path)
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print ("Detected joystick "),joysticks[-1].get_name(),"'"
while keepPlaying:
    if pygame.mixer.music.get_volume() == 0.0:
        pygame.mixer.music.set_volume(0.046875)
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button == pygame.CONTROLLER_BUTTON_A:
                if paused == False:
                    paused = True
                    pygame.mixer.music.pause()
                elif paused == True:
                    pygame.mixer.music.unpause()
                    paused = False
            if event.button == pygame.CONTROLLER_BUTTON_B:
                randomsong()
            if event.button == pygame.CONTROLLER_BUTTON_X:
                paused = True
                pygame.mixer.music.play()
                paused = False
            if event.button == 4:
                if ymod == False:
                    print(pygame.mixer.music.get_volume())
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
                elif ymod == True:
                    pygame.mixer.music.set_volume(0)
            if event.button == 5:
                if ymod == False:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
                elif ymod == True:
                    pygame.mixer.music.set_volume(1.0)
            if event.button == pygame.CONTROLLER_BUTTON_Y:
                ymod = True
        if event.type == pygame.JOYBUTTONUP:
            if event.button == pygame.CONTROLLER_BUTTON_Y:
                ymod = False
    if not pygame.mixer.music.get_busy():
        if paused == False:
            randomsong()
