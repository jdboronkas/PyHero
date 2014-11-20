from PyHero import PyHero

class PyHeroHivemind(object):
    '''
    Main controller of PyHero.
    '''
    def __init__(self):
        self.connectedPyHeros = []

    def connectPyHero(self, ip, pyID):
        '''
        PyHero connectPyHero(str ip, int pyID)
            - returns the PyHero if it was connected successfully
            - returns null if the PyHero was not connected successfully

        Registers a PyHero with this PyHeroHivemind.
        '''
        return PyHero(pyID) # tbi

    def disconnectPyHero(self, pyID):
        '''
        PyHero disconnectPyHero(int pyID)
            - returns the PyHero that was disconnected
            - returns null if the disconnected failed or the pyID did not match

        Un-Registers a PyHero with this PyHeroHivemind.
        '''
        return PyHero(pyID) # tbi

    def loadSong(self, phsFile, pyID):
        '''
        bool loadSong(str phsFile, int pyID)
            - returns true if the load was successful on the given PyHero
            - returns false if the connected PyHero failed to load
                the given song or if the pyID did not match

        Loads a songfile on the given connected PyHero.
        '''
        return True #tbi

    def startSong(self, pyIDList):
        '''
        bool startSong(int[] pyIDList)
            - returns true if the song was able to be played on all
                of the given PyHeros
            - returns false if any of the pyIDs were not found or
                could otherwise not start the song

        Tells each of the given PyHeros to begin playing their loaded songs.
        '''
        return True #tbi
