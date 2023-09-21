import hashlib
import asyncio
import json


from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import redis

from task import predict_toxicity


app = FastAPI()
redis_client = redis.Redis(host='redis', port=6379, db=0)


@app.get('/predict/{message}')
async def predict(message: str):
    message_hash = hashlib.sha256(message.encode()).hexdigest()
    redis_cache = redis_client.get(message_hash)
    if redis_cache:
        return JSONResponse(content=json.loads(redis_cache))
    else:
        task_result = predict_toxicity.apply_async(args=[message])

        while not task_result.ready():
            await asyncio.sleep(0.2)

        if task_result.successful():
            result = task_result.result
            json_data = json.dumps(result)
            redis_client.set(message_hash, json_data)
            return JSONResponse(content=result)
        else:
            raise HTTPException(status_code=500, detail="Task failed")
