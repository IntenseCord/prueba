from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde el archivo .env

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Gestor de Notas"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "BZcHbaEdkQdiis9eTRiapyLpzS6SJcAQZilO7GmClfQ")  # Usar variable de entorno o un valor por defecto
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")  # Ejemplo para SQLite

    class Config:
        case_sensitive = True

settings = Settings()

