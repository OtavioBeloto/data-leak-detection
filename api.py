from fastapi import FastAPI, UploadFile, File, HTTPException
from scanner.detector import detectar_dado_sensivel

app = FastAPI(title="Detector de Dados Vazados API", description="API para detecção de dados sensíveis em arquivos", version="1.0.0")


@app.post("/analisar")
async def analisar_arquivo(arquivo: UploadFile = File(...), mascarar: bool = False):
    if not arquivo.filename.lower().endswith(".txt"):
        raise HTTPException(status_code=400, detail="Apenas arquivos .txt são permitidos")
    conteudo_bytes = await arquivo.read()

    if len(conteudo_bytes) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Arquivo muito grande. Limite (5MB)")

    conteudo = conteudo_bytes.decode("utf-8", errors="replace")
    resultados = detectar_dado_sensivel(conteudo, mascarar=mascarar)

    return {"arquivo": arquivo.filename, "total_resultados": len(resultados), "resultados": resultados}