from SongTranslator import SongTranslator

class SongPlayer(object):
    '''
    Runs translated song files for the PyHeros.
    '''
    def __init__(self):
        self.st = SongTranslator()
        self.phsSongFile = ""
        self.pySongFile = ""

    def loadSong(self, phsFile):
        '''
        bool loadSong(str phsFile)
            - returns true if the file was found, valid, translated, and loaded
            - returns false if the file could not be found, validated,
                translated, or loaded

        Searches for the phsFile, gets it translated, then loads it to be played.
        '''
        return True #tbi

    def startSong(self):
        '''
        bool startSong()
            - returns true if the song was able to be played
            - returns false if there is no song loaded

        Begins playing the song that is currently loaded.
        '''
        return True #tbi
