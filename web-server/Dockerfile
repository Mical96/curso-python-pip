FROM python:3.8

WORKDIR /appy
COPY requirements.txt /appy/requirements.txt

RUN pip install --cache-dir --upgrade -r /appy/requirements.txt

COPY . /appy

CMD ["uvicorn", "main:appy", "--host", "0.0.0.0", "--port", "80"]