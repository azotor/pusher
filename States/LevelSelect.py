import pygame, States, App, Levels

class LevelSelect( States.State ):

    def __init__(self):
        super().__init__()
        self.select = 0

        self.cooldown = App.Cooldown()

    def enter( self ):
        self.cooldown.start( 100 )
        self.surf = pygame.display.get_surface()
        self.select = 0

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
                    case -1:
                        change( States.States.MAIN )
                    case 0:
                        change( States.States.PLAY )
                    case 1:
                        pass
            
            if App.controls.escape:
                change( States.States.MAIN )
        
        if self.select < -1:
            self.select = len( Levels.levels ) - 1
        
        if self.select > len( Levels.levels ) - 1:
            self.select = -1

        self.cooldown.update()

    def render( self ):

        text = App.Config.FONT_TITLE.render( 'Levels', True, App.Config.COLOR_WHITE )
        text_rect = text.get_rect( center = ( App.Config.WINDOW_WIDTH / 2, 50 ) )
        self.surf.blit( text, text_rect )

        w = 200
        h = 70
        gap = 50
        x = ( App.Config.WINDOW_WIDTH - 3 * w - 2 * gap ) / 2
        y = App.Config.WINDOW_HEIGHT / 2 - h * 2 - gap / 2
        cols = 3
        border = 10
        for index, level in enumerate( Levels.levels ):

            rect = (
                x + index % cols * ( w + gap ),
                y + index // cols * ( h + gap ),
                w,
                h
            )

            if self.select == index:
                pygame.draw.rect( self.surf, App.Config.COLOR_DARK, ( rect[ 0 ] - border, rect[ 1 ] - border, rect[ 2 ] + border * 2, rect[ 3 ] + border * 2 ) )
                pygame.draw.rect( self.surf, App.Config.COLOR_PURPLE, ( rect[ 0 ] - border, rect[ 1 ] - border, rect[ 2 ] + border * 2, rect[ 3 ] + border * 2 ), 1 )

            pygame.draw.rect( self.surf, App.Config.COLOR_RED if level.lock else App.Config.COLOR_GREEN, rect, 1 )
            
            text = App.Config.FONT_LEVEL_TITLE.render( level.name, True, App.Config.COLOR_WHITE )
            self.surf.blit( text, ( rect[ 0 ] + 5, rect[ 1 ] + 5 ) )

            text = App.Config.FONT_LEVEL_STATS.render( 'Locked' if level.lock else 'Unlocked', True, App.Config.COLOR_WHITE )
            self.surf.blit( text, ( rect[ 0 ] + 5, rect[ 1 ] + 30 ) )

            text = App.Config.FONT_LEVEL_STATS.render( f'Best time: {level.time} sec', True, App.Config.COLOR_WHITE )
            self.surf.blit( text, ( rect[ 0 ] + 5, rect[ 1 ] + 45 ) )

        text = App.Config.FONT_MAIN.render( 'Back', True, App.Config.COLOR_PURPLE )
        text_rect = text.get_rect( center = ( App.Config.WINDOW_WIDTH / 2 - 200, App.Config.WINDOW_HEIGHT - 50 ) )

        if self.select == -1:
            rect = ( text_rect.centerx - 120 , text_rect.centery - 20, 240, 40 )
            pygame.draw.rect( self.surf, App.Config.COLOR_DARK, rect )
            pygame.draw.rect( self.surf, App.Config.COLOR_PURPLE, rect, 1 )

        self.surf.blit( text, text_rect )