from PyHeroHivemind import PyHeroHivemind
from PyHero import PyHero

server = PyHeroHivemind()

guitar = server.connectPyHero("0.0.0.0", 0)
assert(guitar)

bass = server.connectPyHero("0.0.0.0", 1)
assert(bass)

status = server.loadSong("test_guitar.phs", 0)
assert(status)

status = server.loadSong("test_bass.phs", 1)
assert(status)

status = server.startSong(server.connectedPyHeros)
assert(status)
