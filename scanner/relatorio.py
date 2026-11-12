import json
from pathlib import Path

def salvar_relatorio_json(resultados, caminho):
    caminho = Path(caminho)

    with caminho.open("w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)