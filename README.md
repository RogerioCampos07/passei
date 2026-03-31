# Passei

Projeto Django simples com PostgreSQL, configurado para rodar em Docker (`docker-compose`).

## Visão geral

- Django 6.x
- PostgreSQL 15 (via Docker Compose)
- Estrutura de app: `estudos`
- Configurações por `.env`

---

## Pré-requisitos

- Docker >= 24
- Docker Compose >= 2
- Git (opcional para clonar o repositório)

---

## Preparação local

1. Copie o template de ambiente:

```bash
cp .env-example .env
```

2.Ajuste as variáveis em `.env` se necessário.

- `DEBUG`: `True` em desenvolvimento
- `SECRET_KEY`: chave secreta Django
- `ALLOWED_HOSTS`: `0.0.0.0,localhost,127.0.0.1`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

3.Garanta que `DB_HOST=db` (serviço do Compose).

---

## Rodando com Docker Compose (recomendado)

### 1) Build e start

```bash
docker compose up --build
```

O comando:

- cria e inicia `passei_db` (PostgreSQL) e `passei_web` (Django)
- monta o diretório atual em `/app` (hot reload de código)
- expõe porta `8000` no host

### 2) Migrar banco

Em outro terminal:

```bash
docker compose exec web python manage.py migrate
```

### 3) Criar superusuário

```bash
docker compose exec web python manage.py createsuperuser
```

### 4) Acessar a aplicação

- Navegue em: `http://localhost:8000`
- Admin Django: `http://localhost:8000/admin`

### 5) Parar e remover (opcional)

```bash
docker compose down -v
```

Usar `-v` remove volume e reseta o banco.

---

## Comandos comuns

- rodar testes unitários:
  `docker compose exec web python manage.py test`
- verificar lint (se configurado):
  `docker compose exec web <linter>`

---

## Estrutura de pastas

- `core/`: configuração global do Django
- `estudos/`: app e modelos
- `templates/`: templates HTML
- `db.sqlite3`: banco sqlite local (não usado em Compose)
- `docker-compose.yml`: orquestra Docker
- `Dockerfile`: build da imagem Django

---

## Dockerfile resumido

- imagem base Python
- copia projeto para `/app`
- instala dependências `pyproject.toml`
- expõe porta `8000`

---

## Notas de deploy

- não use `DEBUG=True` em produção
- mantenha `SECRET_KEY` seguro e fora do repositório
- considere `ALLOWED_HOSTS` específico para domínios reais
