from ._version import __version__, version_info
from .font import Font, FontWeight, GoogleFont, PredefinedFonts
from .generator import generate_tag

__all__ = [
    "generate_tag",
    "Font",
    "FontWeight",
    "GoogleFont",
    "PredefinedFonts",
    "__version__",
    "version_info",
]
