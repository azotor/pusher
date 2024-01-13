class Level:
    def __init__( self, name, map, lock = True, time = 0 ):
        self.name = name
        self.size = map[ 'size' ]
        self.tiles = map[ 'tiles' ]
        self.player = map[ 'player' ]
        self.balls = map[ 'balls' ]
        self.holls = map[ 'holls' ]
        self.lock = lock
        self.time = time
    
    def get( self ):
        pass

    def set( self, map, lock, time ):
        self.map = map
        self.lock = lock
        self.time = time