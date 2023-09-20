import hashlib

from fastapi import FastAPI
import redis
from detoxify import Detoxify

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.get('/predict/{message}')
async def predict(message: str):
    message_hash = hashlib.sha256(message.encode()).hexdigest()
    redis_cashe = redis_client.get(message_hash)
    if redis_cashe:
        return redis_cashe
    else:
        model = Detoxify('multilingual', device='cuda')
        prediction = model.predict(message)
        toxic_text = prediction[max(prediction)] > 0.5
        for key in prediction:
            prediction[key] = float(prediction[key])
        return {'toxic_text': toxic_text, 'meta_data': prediction} 
