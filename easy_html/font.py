from dataclasses import dataclass
from typing import List


class FontWeight:
    def __init__(self, weight: int, italic: bool = False):
        self.weight = weight
        self.italic = italic

    def get_weight(self, has_italic: bool = False):
        if self.italic and has_italic:
            return f"1,{self.weight}"

        if not self.italic and has_italic:
            return f"0:{self.weight}"

        return f"{self.weight}"


class Font:
    def __init__(
        self,
        name: str,
        weights: List[FontWeight] = [FontWeight(400)],
        fallback_font: str = "sans-serif",
    ):
        self.font_name = name.replace(" ", "+")
        self.include_italic = next(filter(lambda x: x.italic == True, weights), False)
        self.weights = weights
        self.fallback_font = fallback_font

    def generate_font(self):
        family = f"family={self.font_name}"
        if self.include_italic:
            family += ":ital,wght@"
        else:
            family += ":wght@"

        weights = ";".join(
            [weight.get_weight(self.include_italic) for weight in self.weights]
        )
        family += weights

        return family


class GoogleFont:
    def __init__(self, fonts: List[Font], display: str = "swap"):
        self.fonts = fonts
        self.display = display
        self.familes = "&".join([font.generate_font() for font in self.fonts])
        self.classes = ""

    def get_links(self):
        return (
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'<link href="https://fonts.googleapis.com/css2?{self.familes}&display={self.display}" rel="stylesheet">\n'
        )

    def get_classes(self):
        classes = ""

        for font in self.fonts:
            class_name = font.font_name.replace("+", "_").lower()
            font_name = font.font_name.replace("+", " ")
            classes += (
                f".{class_name}"
                + " { "
                + f"font-family: '{font_name}', {font.fallback_font};"
                " }\n"
            )

        return classes


@dataclass
class PredefinedFonts:
    Roboto: GoogleFont = GoogleFont(
        fonts=[
            Font(
                "Roboto",
                weights=[
                    FontWeight(300),
                    FontWeight(400),
                    FontWeight(500),
                    FontWeight(700),
                ],
            )
        ]
    )

    Poppins: GoogleFont = GoogleFont(
        fonts=[
            Font(
                "Poppins",
                weights=[
                    FontWeight(300),
                    FontWeight(400),
                    FontWeight(500),
                    FontWeight(600),
                    FontWeight(700),
                ],
            )
        ]
    )

    Montserrat: GoogleFont = GoogleFont(
        fonts=[
            Font(
                "Poppins",
                weights=[
                    FontWeight(300),
                    FontWeight(400),
                    FontWeight(500),
                    FontWeight(600),
                    FontWeight(700),
                ],
            )
        ]
    )
