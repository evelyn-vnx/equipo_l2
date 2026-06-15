import sys
import tiktoken
from pathlib import Path

if len(sys.argv) < 2:
    print("Uso: python contar_tokens.py archivo.md")
    sys.exit(1)

archivo = Path(sys.argv[1])

contenido = archivo.read_text(encoding="utf-8")

enc = tiktoken.get_encoding("cl100k_base")

tokens = len(enc.encode(contenido))

print(f"Archivo: {archivo.name}")
print(f"Caracteres: {len(contenido):,}")
print(f"Tokens: {tokens:,}")