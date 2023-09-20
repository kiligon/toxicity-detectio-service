from fastapi import FastAPI

app = FastAPI()

@app.get('/predict/{message}')
async def predict(message: str):
    return 'out'
