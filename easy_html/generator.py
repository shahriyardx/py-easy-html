from bs4 import BeautifulSoup as bs

from .templates import html_page
from .types import ATTRIBUTES, HTML, HTML_TAG_NAME, STYLE


def prettify_html(html: HTML) -> HTML:
    return bs(html, features="html.parser").prettify()


def generate_style(style: STYLE = dict()) -> str:
    styles = ""

    for key, value in style.items():
        styles += f"{key}: {value};"

    return styles


def generate_attributes(attributes: ATTRIBUTES = dict()) -> str:
    attrs = ""

    for key, value in attributes.items():
        attrs += f'{key}="{value}" '

    return attrs


def generate_tag(
    tag_name: HTML_TAG_NAME,
    body: HTML = "",
    self_closing: bool = False,
    class_name: str = "",
    id_name: str = "",
    style: STYLE = dict(),
    prettify: bool = True,
    attributes: ATTRIBUTES = dict(),
) -> HTML:
    styles = generate_style(style)
    attrs = generate_attributes(attributes)
    _id = f' id="{id_name}"' if id_name else ""
    _class = f' class="{class_name}"' if class_name else ""
    _attrs = f" {attrs}" if attrs else ""
    _styles = f' style="{styles}"' if styles else ""

    _template = (
        "<%%tag_name%%%%class%%%%id%%%%style%%%%attr%%/>"
        if self_closing
        else "<%%tag_name%%%%class%%%%id%%%%style%%%%attr%%>%%body%%</%%tag_name%%>"
    )

    html = (
        _template.replace("%%tag_name%%", tag_name)
        .replace("%%class%%", _class)
        .replace("%%id%%", _id)
        .replace("%%style%%", _styles)
        .replace("%%attr%%", _attrs)
    )

    _body = body
    if isinstance(body, list):
        _body = " ".join(body)

    html = html.replace("%%body%%", str(_body))

    if prettify:
        return prettify_html(html)

    return html


def make_page(
    body: HTML,
    title: str = "",
    style: str = "",
    links: str = "",
    font: str = "",
    prettify: bool = True,
) -> HTML:
    _body = body

    if isinstance(body, list):
        _body = " ".join(body)
    html = (
        html_page.replace("%%title%%", title)
        .replace("%%style%%", style + font)
        .replace("%%links%%", links)
        .replace("%%font%%", "")
        .replace("%%body%%", _body)
    )

    if prettify:
        return prettify_html(html)

    return html
