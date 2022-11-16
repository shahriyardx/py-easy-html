from .generator import generate_tag
from .font import Font, FontWeight, GoogleFont, PredefinedFonts
from ._version import __version__, version_info


__all__ = [
    "generate_tag",
    "Font",
    "FontWeight",
    "GoogleFont",
    "PredefinedFonts",
    "__version__",
    "version_info",
]
