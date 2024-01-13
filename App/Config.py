import pygame

pygame.init()

class Config:
    # App data
    TITLE = 'Pusher'
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    FPS = 60

    # Fonts
    FONT_TITLE = pygame.font.SysFont( 'Arial', 48 )
    FONT_MAIN = pygame.font.SysFont( 'Consolas', 32 )
    FONT_LEVEL_TITLE = pygame.font.SysFont( 'Tahoma', 16 )
    FONT_LEVEL_STATS = pygame.font.SysFont( 'Consolas', 12 )

    # Colors
    COLOR_DARK = '#34495e'
    COLOR_DARKER = '#2c3e50'
    COLOR_WHITE = '#ecf0f1'
    COLOR_LIGHT = '#dddddd'
    COLOR_PURPLE = '#9b59b6'
    COLOR_RED = '#e74c3c'
    COLOR_GREEN = '#2ecc71'
    COLOR_BLACK = '#222222'