from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI()

filmes = []

@app.get("/filmes")
async def exibir_filmes():
    return {"filmes": filmes}

@app.post("/filmes")
async def adicionar_filme(filme: Dict):
    if not filme.get("titulo") or not filme.get("ano") or not filme.get("genero"):
        raise HTTPException(status_code=400, detail="Os campos título, ano e gênero são obrigatórios.")
    filmes.append(filme)
    return {"mensagem": "Filme adicionado com sucesso.", "filme": filme}

@app.put("/filmes/{id}")
async def atualizar_filme(id: int, filme: Dict):
    if not filme.get("titulo") or not filme.get("ano") or not filme.get("genero"):
        raise HTTPException(status_code=400, detail="Os campos título, ano e gênero são obrigatórios.")
    if id < 0 or id >= len(filmes):
        raise HTTPException(status_code=404, detail="Filme não encontrado.")
    filmes[id] = filme
    return {"mensagem": "Filme atualizado com sucesso.", "filme": filme}

@app.delete("/filmes/{id}")
async def remover_filme(id: int):
    if id < 0 or id >= len(filmes):
        raise HTTPException(status_code=404, detail="Filme não encontrado.")
    filme_removido = filmes.pop(id)
    return {"mensagem": "Filme removido com sucesso.", "filme": filme_removido}

@app.get("/filmes/{id}")
async def exibir_filme(id: int):
    if id < 0 or id >= len(filmes):
        raise HTTPException(status_code=404, detail="Filme não encontrado.")
    return {"filme": filmes[id]}

@app.post("/filmes/{id}/avaliacoes")
async def adicionar_avaliacao(id: int, avaliacao: Dict):
    if id < 0 or id >= len(filmes):
        raise HTTPException(status_code=404, detail="Filme não encontrado.")
    if not avaliacao.get("usuario") or not avaliacao.get("nota"):
        raise HTTPException(status_code=400, detail="Os campos usuário e nota são obrigatórios.")
    if not isinstance(avaliacao.get("nota"), int) or avaliacao.get("nota") < 0 or avaliacao.get("nota") > 5:
        raise HTTPException(status_code=400, detail="A nota deve ser um número inteiro entre 0 e 5.")
    filmes[id].setdefault("avaliacoes", []).append(avaliacao)
    return {"mensagem": "Avaliação adicionada com sucesso.", "avaliacao": avaliacao}





from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI()

filmes = {}

@app.get("/filmes")
async def exibir_filmes():
    return filmes

@app.post("/filmes")
async def adicionar_filme(titulo: str):
    id_filme = len(filmes) + 1
    filme = {"titulo": titulo}
    filmes[id_filme] = filme
    return filme

@app.delete("/filmes/{id_filme}")
async def remover_filme(id_filme: int):
    if id_filme not in filmes:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    del filmes[id_filme]
    return {"mensagem": "Filme removido com sucesso"}

@app.put("/filmes/{id_filme}")
async def atualizar_filme(id_filme: int, titulo: str):
    if id_filme not in filmes:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    filmes[id_filme]["titulo"] = titulo
    return filmes[id_filme]
