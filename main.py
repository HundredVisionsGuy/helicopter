import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False


# Game Loop
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()

# We're done, close window
pygame.quit()
