from scanner.patterns import PADROES


def mascarar_dados(tipo, valor):
    if tipo == "email":
        usuario, dominio = valor.split("@", 1)
        return f"{usuario[:0]}***@{dominio}"
    if tipo == "cpf":
        digitos = "".join(c for c in valor if c.isdigit())
        return f"***.***.***-{digitos[-2:]}"
    if tipo == "senha":
        return "********"
    return valor

def detectar_dado_sensivel(conteudo, mascarar=True):
    resultados = []
    for numero_linha, linha in enumerate(conteudo.splitlines(), start=1):
        for tipo, padrao in PADROES.items():
            ocorrencias = padrao.finditer(linha)
            for ocorrencia in ocorrencias:
                valor = ocorrencia.group()

                if mascarar:
                    valor = mascarar_dados(tipo, valor)
                
                resultados.append({"tipo": tipo, "linha": numero_linha, "valor": valor})
    return resultados