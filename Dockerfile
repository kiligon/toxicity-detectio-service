FROM nvidia/cuda:11.8.0-base-ubuntu22.04

WORKDIR /app

RUN apt-get update && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh && apt-get -y install python3 python3-pip

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r chore.txt

COPY . /app/

EXPOSE 6379

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
