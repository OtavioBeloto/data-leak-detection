from scanner.patterns import PADROES




def detectar_dado_sensivel(conteudo):
    resultados = []
    for numero_linha, linha in enumerate(conteudo.splitlines(), start=1):
        for tipo, padrao in PADROES.items():
            ocorrencias = padrao.finditer(linha)
            for ocorrencia in ocorrencias:
                valor = ocorrencia.group()
                resultados.append({"tipo": tipo, "linha": numero_linha, "valor": valor})
    return resultados