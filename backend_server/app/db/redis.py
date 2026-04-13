import redis
from app.core.config import settings

# 建立 Redis 連線池
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=int(settings.REDIS_PORT),
    decode_responses=True  # 讓回傳結果自動轉為字串，方便操作
)
