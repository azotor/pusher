import App, States, pygame, webbrowser

class About( States.State ):

    def __init__(self):
        super().__init__()

        self.select = 0
        self.options = [
            'Back',
            'GitHub Repo'
        ]

        self.cooldown = App.Cooldown()

    def enter( self ):
        self.cooldown.start( 100 )
        self.select = 0
        self.surf = pygame.display.get_surface()

    def update( self, change ):

        if not self.cooldown.run:

            if App.controls.left:
                self.select -= 1
                self.cooldown.start( 100 )

            if App.controls.right:
                self.select += 1
                self.cooldown.start( 100 )
            
            if App.controls.select:
                self.cooldown.start( 100 )
                match self.select:
                    case 0:
                        change( States.States.MAIN )
                    case 1:
                        webbrowser.open( "https://github.com/azotor" )
            
            if App.controls.escape:
                change( States.States.MAIN )
        
        if self.select < 0:
            self.select = len( self.options ) - 1
        
        if self.select > len( self.options ) - 1:
            self.select = 0

        self.cooldown.update()

    def render( self ):

        text = App.Config.FONT_TITLE.render( 'About', True, App.Config.COLOR_WHITE )
        text_rect = text.get_rect( center = ( App.Config.WINDOW_WIDTH / 2, 50 ) )
        self.surf.blit( text, text_rect )

        text = App.Config.FONT_MAIN.render( 'Copyright by Kapusta Tomasz', True, App.Config.COLOR_WHITE )
        text_rect = text.get_rect( center = ( App.Config.WINDOW_WIDTH / 2, App.Config.WINDOW_HEIGHT / 2 ) )
        self.surf.blit( text, text_rect )

        x = App.Config.WINDOW_WIDTH / 2 - 200
        for index, option in enumerate( self.options ):
            text = App.Config.FONT_MAIN.render( option, True, App.Config.COLOR_PURPLE )
            text_rect = text.get_rect( center = ( x, App.Config.WINDOW_HEIGHT - 50 ) )

            if index == self.select:
                rect = ( text_rect.centerx - 120 , text_rect.centery - 20, 240, 40 )
                pygame.draw.rect( self.surf, App.Config.COLOR_DARK, rect )
                pygame.draw.rect( self.surf, App.Config.COLOR_PURPLE, rect, 1 )

            self.surf.blit( text, text_rect )
            x += 400