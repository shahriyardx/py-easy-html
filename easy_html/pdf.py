import os
from io import BytesIO

import pdfkit

from .types import HTML


def generate_pdf_from_html(
    html: HTML, as_bytes: bool = False, filename: str = None, path: str = None
):

    if path and filename:
        final_path = os.path.join(path, filename)
        return pdfkit.PDFKit(html, "string").to_pdf(final_path)

    if as_bytes:
        io = BytesIO()
        io.write(pdfkit.PDFKit(html, "string").to_pdf())
        io.seek(0)

        return io
