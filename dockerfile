FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV SECRET_KEY=supersecret123

EXPOSE 5000

CMD ["python", "app.py"]
