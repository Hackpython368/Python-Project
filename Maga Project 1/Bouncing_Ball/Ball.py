import pygame 

pygame.init()

# Game Variable 
Screen_Width = 1100
Screen_Height = 510


# Colour 
Black = (0,0,0)
Red = (255,0,0)
Blue = (0,0,255)
Ball_X = 30
Ball_Y = 30
Player_X = 0
Player_Y = 480
Ball_X_Add = 1
Ball_Y_Add = 1
Player_Left = False
Player_Right = False 
Player_Score = 0
GameLoop = True



Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Hello world")

font = pygame.font.Font(None,22)

Clock = pygame.time.Clock()

while GameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_Left = True
            if event.key == pygame.K_RIGHT:
                Player_Right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Player_Left = False
            if event.key == pygame.K_RIGHT:
                Player_Right = False

    if Player_Right :
        Player_X += 10
    if Player_Left :
        Player_X -= 10

    text = font.render("SCORE : {}".format(Player_Score),0,Red)
    # Player Control 
    if (Player_X<=Ball_X and Player_Y==Ball_Y) and Player_X+200>Ball_X:
        Ball_Y_Add *= -1
        Player_Score += 10

    # Fixed 
    if Ball_Y<=20:
        Ball_Y_Add *= -1
    if Ball_X>=(Screen_Width-20) or Ball_X<=20:
        Ball_X_Add *= -1

    # Game Over
    if Ball_Y>(Screen_Height+30):
        GameLoop = False
        pygame.quit()
        print("GameOver")
        break


    Ball_X += Ball_X_Add
    Ball_Y += Ball_Y_Add
    Screen.fill(Black)
    pygame.draw.circle(Screen,Red,(Ball_X,Ball_Y),19)
    Screen.blit(text,(10,10))
    pygame.draw.rect(Screen,Blue,(Player_X,Player_Y,200,30))
    Clock.tick(180)
    pygame.display.update()