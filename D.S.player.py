import pygame
from pygame import *
from speak import speak
import webbrowser
speak("Welcome to D.S. player")
pygame.init()
screen = pygame.display.set_mode((1100, 600))

pygame.display.set_caption("D.S. Player || I Love Music!")

def ad():
    speak("please subscribe to Tele Coder channel to get more free apps like this")
ad()
# mixer.music.load("te.mp3")
# mixer.music.play(-1)

red = (255, 0, 0)
green = (0, 200, 0)
black = (0,0,0)
white = (255, 255, 255)
blue = (0,0,255)


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()



def button(msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action == "animals":
            speak("okay playing")
            mixer.music.load("dd.mp3")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "ego":
            mixer.music.load("Ego.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "chmu":
            speak("i can't do that!")
        elif click[0] == 1 and action == "UTS":
            mixer.music.load("1.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "Thun":
            mixer.music.load("thun.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "be":
            mixer.music.load("be.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "ch":
            mixer.music.load("ch.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "ct":
            mixer.music.load("ct.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "hap":
            mixer.music.load("hap.mp3")
            speak("okay playing")
        
            mixer.music.play(-1)
        elif click[0] == 1 and action == "ut":
            mixer.music.load("ut.mp3")
            speak("okay playing")
        
            mixer.music.play(-1)
        elif click[0] == 1 and action == "bg":
            mixer.music.load("bg.mp3")
            speak("okay playing")
        
            mixer.music.play(-1)
        elif click[0] == 1 and action == "otf":
            mixer.music.load("otf.mp3")
            speak("okay playing")
        
            mixer.music.play(-1)
        elif click[0] == 1 and action == "eti":
            mixer.music.load("eti.mp3")
            speak("okay playing")
        
            mixer.music.play(-1)
        elif click[0] == 1 and action == "fd":
            mixer.music.load("fd.mp3")
            speak("okay playing")
        
            mixer.music.play(-1)
        elif click[0] == 1 and action == "da":
            mixer.music.load("da.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "w":
            mixer.music.load("ww.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "bulletproof":
            mixer.music.load("orig.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "danceMonkey":
            mixer.music.load("dm.mp3")
            speak("okay playing")

            mixer.music.play(-1)
        elif click[0] == 1 and action == "fs":
            mixer.music.load("fs.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "pd":
            mixer.music.load("pd.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "te":
            mixer.music.load("te.mp3")
            speak("okay playing")
            mixer.music.play(-1)
        elif click[0] == 1 and action == "supp":
            webbrowser.open("https://www.youtube.com/channel/UCjW0sdo4VpaV0QCn9-8vSYg")
        elif click[0] == 1 and action == "quit":
            pygame.quit()
            quit()
            ad()
            speak("have a nice day!")
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


clock = pygame.time.Clock()

intro = True


while intro:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            speak("have a nice day!")
    button("Animals", 50, 50, 200, 50, green, red, "animals")
    button("JOY TO THE WORLD", 50, 250, 200, 50, green, red, "fs")
    button("Dance Monkey", 50, 150, 200, 50, green, red, "danceMonkey")
    button("DA Agust", 50, 350, 200, 50, green, red, "da")
    button("Waka Waka", 50, 450, 200, 50, green, red, "w")
    


    button("Ego", 300, 50, 200, 50, white, blue, "ego")
    button("Under the sea", 300, 150, 200, 50, white, blue, "UTS")
    button("Bulletproof", 300, 250, 200, 50, white, blue, "bulletproof")
    button("Try Everything", 300, 350, 200, 50, white, blue, "te")
    button("Playdate To You", 300, 450, 200, 50, white, blue, "pd")

    button("Thunder", 550, 50, 200, 50, green, red, "Thun")
    button("Chandelier", 550, 250, 200, 50, green, red, "ch")
    button("Happy", 550, 150, 200, 50, green, red, "hap")
    button("Believer", 550, 350, 200, 50, green, red, "be")
    button("Cheap Thrills", 550, 450, 200, 50, green, red, "ct")
    


    button("UpTown Funk", 800, 50, 200, 50, white, blue, "ut")
    button("Everything I wanted", 800, 150, 200, 50, white, blue, "eti")
    button("Bad Guy", 800, 250, 200, 50, white, blue, "bg")
    button("Faded", 800, 350, 200, 50, white, blue, "fd")
    button("On The Floor", 800, 450, 200, 50, white, blue, "otf")

    button("Quit", 800,540, 100, 50, white, blue, "quit")
    button("Support", 400,540, 100, 50, white, blue, "supp")
    button("Change Music", 0,540, 200, 50, white, blue, "chmu")
    pygame.display.update()
    clock.tick(15)


