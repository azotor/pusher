import math, States, Entities, Levels, App

class Play( States.State ):
    
    def __init__( self ):
        super().__init__()
    
    def enter( self ):
        self.currentLevel = 0
        self.map = Entities.Map( Levels.levels[ self.currentLevel ] )
        self.player = Entities.Player()
        self.player.pos = self.map.getPlayerStart()
        self.balls = []
        self.holls = []
        for ballCord in self.map.map.balls:
            ball = Entities.Ball()
            ball.pos = self.map.getEntityStart( ballCord[ 0 ], ballCord[ 1 ] )
            self.balls.append( ball )
        for hollCord in self.map.map.holls:
            holl = Entities.Holl()
            holl.pos = self.map.getEntityStart( hollCord[ 0 ], hollCord[ 1 ] )
            self.holls.append( holl )

    def update( self, change ):
        self.player.update()
        self.player.pos = self.map.getNewPosIfCollideWithNeighbors( self.player )
        for ball in self.balls:
            if App.Collision.circleToCircle( self.player.pos[ 0 ], self.player.pos[ 1 ], self.player.radius, ball.pos[ 0 ], ball.pos[ 1 ], ball.radius ):
                angle = App.Collision.circleToCircleCollisionDirection( self.player.pos[ 0 ], self.player.pos[ 1 ], ball.pos[ 0 ], ball.pos[ 1 ] )
                ball.convertAngleToDirection( angle + math.pi )
            
            ball.update()

    def render( self ):
        self.map.render()
        for ball in self.balls: ball.render()
        for holl in self.holls: holl.render()
        self.player.render()