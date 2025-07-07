from pydantic import BaseModel, EmailStr  
# Importa ferramentas para validar dados
from datetime import datetime  
# Importa para trabalhar com datas
from typing import Optional  
# Importa para dizer que um campo pode ser vazio

class UserBase(BaseModel):  
    # Modelo base para os dados do usuário
    full_name: Optional[str] = None  
    # Nome completo (pode ser vazio)
    role: str = "member"  
    # Função na biblioteca (padrão é "member")

class UserCreate(BaseModel):  
    # Modelo para criar um usuário
    email: EmailStr  
    # Email (tem que ser um email válido)
    password: str  
    # Senha
    full_name: Optional[str] = None  
    # Nome completo (opcional)
    role: str = "member"  
    # Função (padrão é "member")

class UserUpdate(BaseModel):  
    # Modelo para atualizar um usuário
    full_name: Optional[str] = None 
    # Nome completo (opcional)
    role: Optional[str] = None  
    # Função (opcional)

class User(UserBase):  # Modelo completo do usuário
    id: str  
    # ID do usuário (vem do Supabase)
    email: EmailStr  
    # Email
    updated_at: Optional[datetime] = None  
    # Quando o perfil foi atualizado

    class Config:  
        # Configuração extra
        from_attributes = True 
        # Permite usar dados do banco diretamente