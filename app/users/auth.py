from fastapi_users.authentication import CookieTransport, AuthenticationBackend, RedisStrategy
import redis.asyncio as redis
from app.config import get_settings

settings = get_settings()

redis_client = redis.from_url(settings.redis_url, decode_responses=True)

cookie_transport = CookieTransport(cookie_name="auth", cookie_max_age=3600)

def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis_client, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="redis_cookie",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)