from SongPlayer import SongPlayer

class PyHero(object):
    '''
    Actual PyHero player.
    '''
    def __init__(self, pyID):
        self.pyID = pyID
        self.sp = SongPlayer()
        self.loadedSong = ""

    def loadSong(self, phsFile):
        '''
        bool loadSong(str phsFile)
            - returns true if the load was successful on the given PyHero
            - returns false if this PyHero failed to load the given song

        Loads a songfile on this PyHero.
        '''
        return True #tbi

    def startSong(self):
        '''
        bool startSong()
            - returns true if the song was able to be played by this PyHero
            - returns false if this PyHero could not start the song

        Tells this PyHero to begin playing their loaded song.
        '''
        return True #tbi
