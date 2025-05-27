import re

def corresponde(texto: str, padrao: str) -> bool:
    return re.match(padrao, texto) is not None