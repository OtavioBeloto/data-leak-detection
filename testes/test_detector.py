from scanner.detector import detectar_dado_sensivel

def test_detectar_email():
    conteudo = "Contato: jonas@email.com"

    resultado = detectar_dado_sensivel(conteudo, mascarar=False)


    assert len(resultado) == 1
    assert resultado[0]["tipo"] == "email"
    assert resultado[0]["valor"] == "jonas@email.com"

def test_detectar_cpf():
    conteudo = "CPF: 123.456.789-00"

    resultado = detectar_dado_sensivel(conteudo, mascarar=False)

    assert len(resultado) == 1
    assert resultado[0]["tipo"] == "cpf"
    assert resultado[0]["valor"] == "123.456.789-00"

def test_detectar_senha():
    conteudo = "senha: teste123456"

    resultado = detectar_dado_sensivel(conteudo, mascarar=False)
    
    assert len(resultado) == 1
    assert resultado[0]["tipo"] == "senha"
    assert resultado[0]["valor"] == "senha: teste123456"

def test_mascaramento_email():
    conteudo = "Contato: jonas@email.com"

    resultado = detectar_dado_sensivel(conteudo, mascarar=True)

    assert resultado[0]["valor"] == "***@email.com"

def test_mascaramento_cpf():
    conteudo = "CPF: 123.456.789-00"

    resultado = detectar_dado_sensivel(conteudo, mascarar=True)

    assert resultado[0]["valor"] == "***.***.***-00"

def test_mascaramento_senha():
    conteudo = "senha: teste123456"

    resultado = detectar_dado_sensivel(conteudo, mascarar=True)

    assert resultado[0]["valor"] == "********"

def test_nenhum_dado_sensivel():
    conteudo = "Olá mundo"

    resultados = detectar_dado_sensivel(conteudo,mascarar=False)

    assert resultados == []


def test_varios_dados_na_mesma_linha():
    conteudo = "Email: teste@gmail.com CPF: 123.456.789-10 senha: teste123456"

    resultados = detectar_dado_sensivel(conteudo,mascarar=False)

    assert len(resultados) == 3
    assert resultados[0]["tipo"] == "email"
    assert resultados[1]["tipo"] == "cpf"
    assert resultados[2]["tipo"] == "senha"
