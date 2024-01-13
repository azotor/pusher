import States

class Preload( States.State ):

    def update( self, change ):
        change( States.States.MAIN )