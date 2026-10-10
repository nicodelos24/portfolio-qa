#!/usr/bin/env python3
"""Comprueba documentos y CV; no ejecuta pruebas de los productos."""
from pathlib import Path
from html.parser import HTMLParser
import base64
import re
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CV = ROOT / 'cv'


class BodyText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_body = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            self.in_body = True
        if self.in_body and tag in ('p', 'li', 'h1', 'h2', 'br', 'td'):
            self.parts.append(' ')

    def handle_endtag(self, tag):
        if tag == 'body':
            self.in_body = False
        if self.in_body and tag in ('p', 'li', 'h1', 'h2', 'td'):
            self.parts.append(' ')

    def handle_data(self, data):
        if self.in_body:
            self.parts.append(data)


def normalized(text):
    return re.sub(r'\s+|•', '', unicodedata.normalize('NFC', text))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    docs = list(ROOT.glob('*.md')) + list(CV.glob('*.md'))
    for doc in docs:
        text = doc.read_text()
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if re.match(r'https?://|mailto:|#', target):
                continue
            path = target.split('#')[0]
            require((doc.parent / path).exists(), f'Enlace roto: {doc.name} → {target}')
    html = (CV / 'CV-Nicolas-De-Los-Santos-QA.html').read_text()
    photo = re.search(r'src="data:image/png;base64,([^"]+)"', html)
    require(photo is not None, 'Falta la foto incrustada en el HTML')
    require(base64.b64decode(photo[1]) == (CV / 'foto-perfil.png').read_bytes(),
            'La foto del HTML no coincide con foto-perfil.png')
    parser = BodyText()
    parser.feed(html)
    html_text = ''.join(parser.parts)
    markdown = (ROOT / 'cv-qa.md').read_text()
    markdown = re.sub(r'^#{1,6}\s+|^-\s+', '', markdown, flags=re.M).replace('**', '')
    require(normalized(markdown) == normalized(html_text), 'El Markdown y el HTML tienen distinto texto')
    pdf = CV / 'CV-Nicolas-De-Los-Santos-QA.pdf'
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    require(re.search(r'Pages:\s+1\b', info), 'El PDF debe tener una página')
    require('(A4)' in info, 'El PDF debe ser A4')
    pdf_text = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
    require(normalized(html_text) == normalized(pdf_text), 'El HTML y el PDF tienen distinto texto')
    images = subprocess.check_output(['pdfimages', '-list', str(pdf)], text=True)
    require(re.search(r'^\s+1\s+\d+\s+image', images, re.M), 'No hay foto incrustada en el PDF')
    if (ROOT / '.git').exists():
        private = subprocess.check_output(['git', 'ls-files', '--', 'privado'], cwd=ROOT, text=True)
        require(not private.strip(), 'Hay material privado incluido en Git')
    print('OK: enlaces internos, foto, Markdown/HTML/PDF coincidentes y CV de una página A4.')


if __name__ == '__main__':
    main()
