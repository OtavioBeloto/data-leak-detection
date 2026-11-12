from pathlib import Path


def ler_arquivo_txt(caminho):
    caminho = Path(caminho)

    return caminho.read_text(encoding="utf-8", errors="replace")




