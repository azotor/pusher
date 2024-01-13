import States

class StatesManager:

    current = None

    def __init__( self ):
        self.change( States.States.PRELOAD )
    
    def change( self, state ):
        self.current = state
        self.current.enter()

    def update( self ):
        self.current.update( self.change )
    
    def render( self ):
        self.current.render()