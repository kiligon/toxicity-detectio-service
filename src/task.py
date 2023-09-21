from detoxify import Detoxify
from celery import Celery
import torch

app = Celery(
    'celery_app',
    broker='amqp://guest:guest@rabbitmq:5672/', # must use another user and password in production
    backend='rpc://'
)


@app.task
def predict_toxicity(text):
    """
    Predict toxicity of a given text.

    This Celery task uses the 'Detoxify' library to predict the toxicity of the provided text. It loads a pre-trained
    'multilingual' model on the GPU if available, predicts the toxicity, and returns the result.

    Parameters:
        text (str): The text for which toxicity is to be predicted.

    Returns:
        dict: A dictionary containing the toxicity prediction result and associated meta-values.
            - 'toxic_text' (str): Either 'Toxic' or 'Nontoxic' based on the prediction threshold.
            - 'meta_value' (dict): A dictionary with toxicity scores for various categories.
    """
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = Detoxify('multilingual', device=device)
    prediction = model.predict(text)
    toxic_text = 'Toxic' if prediction[max(prediction)] > 0.5 else 'Nontoxic'
    for key in prediction:
        prediction[key] = float(prediction[key])
    return {'toxic_text': toxic_text, 'meta_value': prediction}
