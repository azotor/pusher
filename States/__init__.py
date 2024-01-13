from States.State import State
from States.Preload import Preload
from States.Main import Main
from States.About import About
from States.LevelSelect import LevelSelect
from States.Play import Play

class States:
    PRELOAD = Preload()
    MAIN = Main()
    ABOUT = About()
    LEVELSELECT = LevelSelect()
    PLAY = Play()