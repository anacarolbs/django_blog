# main_fastapi.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional # 'Optional' substitui 'str | None = None' para compatibilidade com Python mais antigo se necessário, mas 'str | None' é moderno.

# 1. Crie uma instância do FastAPI
app = FastAPI(
    title="Minha API de Blog com FastAPI",
    description="Uma API para gerenciar posts, inspirada no projeto Django.",
    version="0.1.0",
)

# --- Modelos Pydantic para nossos dados ---
# Estes modelos definem a estrutura dos dados que esperamos nas requisições
# e que enviaremos nas respostas.

class PostBase(BaseModel):
    title: str
    body: str
    # Poderíamos adicionar outros campos como category, author_name etc.

class PostCreate(PostBase):
    # Campos específicos para criação, se houver
    pass

class PostResponse(PostBase):
    id: int
    # Podemos adicionar outros campos que vêm do "banco de dados" como created_on etc.

    # Configuração para permitir que Pydantic funcione bem com objetos ORM (não estamos usando ORM aqui ainda, mas é bom saber)
    class Config:
        from_attributes = True # Anteriormente orm_mode = True, mudou em Pydantic v2

# --- "Banco de Dados" em Memória ---
# Para simular o armazenamento de posts
fake_posts_db = [
    {"id": 1, "title": "Post de Exemplo 1 do FastAPI", "body": "Conteúdo do post 1."},
    {"id": 2, "title": "FastAPI é Rápido!", "body": "Realmente, muito rápido."},
    {"id": 3, "title": "Aprendendo Pydantic", "body": "Modelos de dados com Python."},
]
next_post_id = 4


# --- Endpoints da API para Posts ---

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Blog com FastAPI!"}

# 1. Listar todos os posts
@app.get("/fastapi/posts/", response_model=List[PostResponse])
async def list_posts():
    """
    Retorna uma lista de todos os posts.
    """
    return fake_posts_db

# 2. Criar um novo post
@app.post("/fastapi/posts/", response_model=PostResponse, status_code=201)
async def create_post(post_data: PostCreate):
    """
    Cria um novo post.
    Espera um JSON no corpo da requisição com 'title' e 'body'.
    """
    global next_post_id
    new_post = {"id": next_post_id, **post_data.model_dump()}
    fake_posts_db.append(new_post)
    next_post_id += 1
    return new_post

# 3. Obter um post específico pelo ID
@app.get("/fastapi/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    """
    Retorna os detalhes de um post específico baseado no seu ID.
    """
    for post_in_db in fake_posts_db:
        if post_in_db["id"] == post_id:
            return post_in_db
    raise HTTPException(status_code=404, detail="Post não encontrado")

# 4. Atualizar um post existente (PUT - substitui o recurso inteiro)
@app.put("/fastapi/posts/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, post_data: PostBase): # PostBase para os dados de atualização
    """
    Atualiza um post existente.
    Substitui todos os campos do post com os dados fornecidos.
    """
    for index, post_in_db in enumerate(fake_posts_db):
        if post_in_db["id"] == post_id:
            updated_post = {"id": post_id, **post_data.model_dump()}
            fake_posts_db[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post não encontrado")

# 5. Deletar um post
@app.delete("/fastapi/posts/{post_id}", status_code=204)
async def delete_post(post_id: int):
    """
    Deleta um post existente.
    """
    global fake_posts_db
    post_found = False
    # Filtra a lista para remover o post com o ID correspondente
    # (Criando uma nova lista sem o item a ser deletado)
    new_db = []
    for post_in_db in fake_posts_db:
        if post_in_db["id"] == post_id:
            post_found = True
        else:
            new_db.append(post_in_db)
    
    if not post_found:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    
    fake_posts_db = new_db
    return # Retorna status 204 No Content (sem corpo na resposta)
