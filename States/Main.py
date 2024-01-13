import App, States, pygame

class Main( States.State ):

    def __init__(self):
        super().__init__()

        self.select = 0
        self.options = [
            'Levels',
            'About',
            'Quit'
        ]

        self.cooldown = App.Cooldown()

    def enter( self ):
        self.cooldown.start( 100 )
        self.select = 0
        self.surf = pygame.display.get_surface()

    def update( self, change ):

        if not self.cooldown.run:

            if App.controls.up:
                self.select -= 1
                self.cooldown.start( 100 )

            if App.controls.down:
                self.select += 1
                self.cooldown.start( 100 )
            
            if App.controls.select:
                self.cooldown.start( 100 )
                match self.select:
                    case 0:
                        change( States.States.LEVELSELECT )
                    case 1:
                        change( States.States.ABOUT )
                    case 2:
                        App.events.running = False
        
        if self.select < 0:
            self.select = len( self.options ) - 1
        
        if self.select > len( self.options ) - 1:
            self.select = 0

        self.cooldown.update()

    def render( self ):

        text = App.Config.FONT_TITLE.render( App.Config.TITLE, True, App.Config.COLOR_WHITE )
        text_rect = text.get_rect( center = ( App.Config.WINDOW_WIDTH / 2, 50 ) )
        self.surf.blit( text, text_rect )

        y = App.Config.WINDOW_HEIGHT / 2
        for index, option in enumerate( self.options ):
            text = App.Config.FONT_MAIN.render( option, True, App.Config.COLOR_PURPLE )
            text_rect = text.get_rect( center = ( App.Config.WINDOW_WIDTH / 2, y ) )

            if index == self.select:
                rect = ( text_rect.centerx - 120 , text_rect.centery - 20, 240, 40 )
                pygame.draw.rect( self.surf, App.Config.COLOR_DARK, rect )
                pygame.draw.rect( self.surf, App.Config.COLOR_PURPLE, rect, 1 )

            self.surf.blit( text, text_rect )
            y += 45