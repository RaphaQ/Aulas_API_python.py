from fastapi import APIRouter, HTTPException  # Importa ferramentas para criar rotas e erros
from app.core.database import get_supabase  # Importa a conexão com o Supabase
from app.models.user import UserCreate  # Importa o modelo para criar usuários
from supabase import Client  # Importa o tipo Client do Supabase

router = APIRouter(prefix="/auth", tags=["Auth"])  # Cria um grupo de rotas com prefixo /auth

@router.post("/signup", status_code=201)  # Rota para cadastrar usuário
async def signup(user: UserCreate):  # Recebe os dados do usuário
    supabase: Client = get_supabase()  # Conecta ao Supabase
    try:  # Tenta cadastrar o usuário
        # Cadastra no sistema de autenticação do Supabase
        auth_response = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password
        })
        if not auth_response.user:  # Se falhar, mostra erro
            raise HTTPException(status_code=400, detail="Failed to create user")
        
        # Salva o perfil na tabela profiles
        profile_data = {
            "id": auth_response.user.id,  # ID do usuário
            "full_name": user.full_name,  # Nome
            "role": user.role  # Função
        }
        supabase.table("profiles").insert(profile_data).execute()
        
        return {"message": "User created successfully"}  # Sucesso!
    except Exception as e:  # Se der erro, mostra o problema
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")  # Rota para fazer login
async def login(email: str, password: str):  # Recebe email e senha
    supabase: Client = get_supabase()  # Conecta ao Supabase
    try:  # Tenta fazer login
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        if not response.session:  # Se falhar, mostra erro
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return {
            "access_token": response.session.access_token,  # Token para usar a API
            "token_type": "bearer"  # Tipo do token
        }
    except Exception as e:  # Se der erro, mostra o problema
        raise HTTPException(status_code=401, detail="Invalid email or password")