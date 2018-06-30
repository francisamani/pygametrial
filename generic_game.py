import pygame

# Initialising the module
pygame.init()

# Placing limits to the display using a Tupple
gameDisplay = pygame.display.set_mode((800,600))

# Setting the name of the game
pygame.display.set_caption('Car Chasers')

# Setting the timing of the game
clock = pygame.time.Clock()

# Placing Crashing as False
crashed = False

while not crashed:
    # Placing an event to track mouse and keyboard presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # To update the entire diplay
    pygame.display.update()

    # Setting the in-game frames per second
    clock.tick(60)

# Quiting the game
pygame.quit()
quit()
