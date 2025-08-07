## Сделайте .env файл. 

# PostgreSQL
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=
DATABASE_USER=postgres
DATABASE_PASSWORD=

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# App
APP_HOST=127.0.0.1
APP_PORT=8000
DEBUG=True

# Auth
SECRET=super-secret-value


## И сделайте контейнер Redis в Docker

docker run -d --name redis-fastapi -p 6379:6379 redis

## И сделайте миграцию alembic