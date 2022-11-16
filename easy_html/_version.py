from collections import namedtuple

__version__ = "0.0.2"

VersionInfo = namedtuple("VersionInfo", "major minor macro release")

version_info = VersionInfo(*map(int, __version__.split(".")), "alpha")
