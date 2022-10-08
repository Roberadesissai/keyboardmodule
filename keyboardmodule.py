def getKey(keyName):
    ans= False
    running = True
    for event in pygame.event.get():  # error is here
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    if running:
        pygame.display.flip()
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans