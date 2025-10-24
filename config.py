import os

class Config:
    raw_url = os.getenv("DATABASE_URL", "")
    if raw_url.startswith("postgres://"):
        raw_url = raw_url.replace("postgres://", "postgresql://", 1)

    if raw_url and "sslmode=" not in raw_url:
        sep = "&" if "?" in raw_url else "?"
        raw_url = f"{raw_url}{sep}sslmode=require"

    SQLALCHEMY_DATABASE_URI = raw_url or "postgresql://user:pass@localhost:5432/precificacao"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
