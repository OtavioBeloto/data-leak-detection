Data Leak Detection

Projeto desenvolvido em Python para identificar possíveis dados sensíveis em arquivos de texto.

FUNCIONALIDADES
- Detecção de endereços de e-mai, Cpf e senhas identificadas por palavras chave
- Mascaramento de dados sensiveis
- Leitura de arquivos txt
- Exportaçao de relatorios json
- Api rest desenvolvida usando FastAPI
- Testes com Pytest

Linguagens e Tecnologias Usadas
- Python
- Regular Expressions (Regex)
- FastAPI
- Uvicorn
- Pytest
- JSON
- HTTPX

INSTALAÇAO

Clone o repositório:

    git clone URL_DO_SEU_REPOSITORIO

Entre na pasta do projeto:

    cd data-leak-detection

Instale as dependências:
    
    pip install -r requirements.txt


EXECUTAR SCANNER (Selecione um arquivo TXT para iniciar a análise.)
    
    python main.py
    

EXECUTAR API

- iniciar servidor
    
    python -m uvicorn api:app --reload

- Acesse a documentação interativa:
    
    http://127.0.0.1:8000/docs

EXECUTANDO OS TESTES (Execute na raiz do projeto)
    
    python -m pytest testes/ -v

OBJETIVO
    Este projeto foi desenvolvido com o objetivo de praticar programação em Python, processamento de arquivos, expressões regulares, desenvolvimento de APIs e testes automatizados.

OBSERVAÇAO
    O detector utiliza padrões para identificar possíveis dados sensíveis. Os resultados devem ser tratados como candidatos à revisão, não como uma validação definitiva de vazamentos.