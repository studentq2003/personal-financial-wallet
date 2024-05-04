FROM python:3.10-alpine

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .

CMD ["python", "cli.py"]