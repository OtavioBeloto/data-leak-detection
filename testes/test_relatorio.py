import json 
from scanner.relatorio import salvar_relatorio_json

def test_salvar_relatorio_json(tmp_path):
    resultados = [
        {
            "tipo": "email",
            "linha": 10,
            "valor": "usuario@example.com"
        }
    ]
    #tmp_path cria uma pasta temporaria para executar o teste
    caminho = tmp_path / "relatorio.json"

    salvar_relatorio_json(resultados, caminho)


    assert caminho.exists()

    with caminho.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    assert dados == resultados