class SongTranslator(object):
    '''
    Translates song files from the PyHeroScript (.phs) file format
    to a generated/runable Python Script (.py) file format.
    '''
    def __init__(self):
        pass # do nothing

    def translateSong(self, phsFile):
        '''
        bool loadSong(str phsFile)
            - returns true if the file was found, valid, and translated
            - returns false if the file could not be found, validated, or
                translated

        Translates the given .phs file into a runnable .py file.
        '''
        instrument = ""
        bpm = 0
        
        song = open(phsFile, 'r')

        for line in openfile:
            status = validate(line)
            if status:
                status = translateLine(line)
                if not status: # Line had errors on it..
                    print "ERROR:: .phs Syntax error.. quitting"
                    print line
                    return False
        
        return True #tbi

    def validate(self, phsLine):
        if phsLine == "guitar" or phsLine == "bass":
            return True
        
        return True # tbi

    def translateLine(self, phsLine):
        return True # tbi
