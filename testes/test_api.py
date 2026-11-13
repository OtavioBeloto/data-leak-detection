
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_analisar_arquivo_txt():
    conteudo = """
    Meu email é teste@gmail.com
    Meu CPF é 123.456.789-10
    Minha senha: teste123456
    """

    response = client.post("/analisar",files={"arquivo":("exemplo.txt",conteudo.encode("utf-8"),"text/plain")})

    assert response.status_code == 200

    dados = response.json()

    assert dados["total_resultados"] == 3
    assert dados["resultados"][0]["tipo"] == "email"
    assert dados["resultados"][1]["tipo"] == "cpf"
    assert dados["resultados"][2]["tipo"] == "senha"


def test_rejeitar_arquivo_que_nao_seja_txt():
    response = client.post("/analisar",files={"arquivo":("exemplo.pdf",b"conteudo de teste","application/pdf")})

    assert response.status_code == 400
