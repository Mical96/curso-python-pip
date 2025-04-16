FROM python:3.8

WORKDIR /appy
COPY requirements.txt /appy/requirements.txt

RUN pip install --cache-dir --upgrade -r /appy/requirements.txt

COPY . /appy

CMD bash -c "while true; do sleep 1; done" 