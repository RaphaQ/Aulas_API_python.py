from pydantic_settings import BaseSettings  

# Ferramenta para ler o .env

class Settings(BaseSettings):  # Classe para guardar as chaves
    supabase_url: str  # Guarda a URL do Supabase
    supabase_key: str  # Guarda a chave do Supabase

    class Config:  # Configurações extras
        env_file = ".env"  # Diz que as chaves estão no .env
        env_file_encoding = "utf-8"  # Formato do texto

settings = Settings()  # Carrega as chaves do .env