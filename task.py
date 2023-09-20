from detoxify import Detoxify
from celery import Celery


app = Celery(
    'celery_app',
    broker='amqp://guest:guest@rabbitmq:5672/',
    backend='rpc://'
)


@app.task
def predict_toxicity(text):
    model = Detoxify('multilingual', device='cuda')
    prediction = model.predict(text)
    toxic_text = prediction[max(prediction)] > 0.5
    for key in prediction:
        prediction[key] = float(prediction[key])
    return {'toxic_text': toxic_text, 'meta_value': prediction}
