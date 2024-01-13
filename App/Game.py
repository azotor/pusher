import pygame, sys, App

class Game:

    def __init__( self ):
        self.clock = pygame.time.Clock()
        self.surf = pygame.display.set_mode( ( App.Config.WINDOW_WIDTH, App.Config.WINDOW_HEIGHT ) )
        pygame.display.set_caption( App.Config.TITLE )
        self.statesManager = App.StatesManager()

        self.loop()

    def loop( self ):
        while App.events.running:
            App.events.update()

            self.update()
            self.render()

            pygame.display.update()
            self.clock.tick( App.Config.FPS )

        pygame.quit()
        sys.exit()

    def update( self ):
        self.statesManager.update()

    def render( self ):
        self.surf.fill( App.Config.COLOR_DARKER )
        self.statesManager.render()