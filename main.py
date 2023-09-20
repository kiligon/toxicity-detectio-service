import hashlib

from fastapi import FastAPI
import redis

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.get('/predict/{message}')
async def predict(message: str):
    message_hash = hashlib.sha256(message.encode()).hexdigest()
    redis_cashe = redis_client.get(message_hash)
    if redis_cashe:
        return redis_cashe
    else:
        pass
    return 'out'
