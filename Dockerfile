# 1. Imagem base com Python 3.13 (O futuro é agora!)
FROM python:3.13-slim

# 2. Variáveis de ambiente cruciais para o Linux e Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/tmp/poetry_cache'

# 3. Define a Arena de trabalho
WORKDIR /app

# 4. Instala dependências de sistema para o Postgres no Linux
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 5. Instala o Poetry na versão mais recente para suportar o [project]
RUN pip install "poetry>=2.0.0"

# 6. Copia os arquivos de configuração (Raiz do projeto para a Raiz do container)
COPY pyproject.toml poetry.lock* /app/

# 7. Instala as dependências (Django 5.2, Pydantic, Psycopg2)
# Como você usa a seção [project], o Poetry instala as 'dependencies' automaticamente
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# 8. Copia o restante do código (as pastas core, estudos, etc.)
COPY . /app/

# 9. Abre o portão do estádio
EXPOSE 8000

# 10. Apita o início do jogo!
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]