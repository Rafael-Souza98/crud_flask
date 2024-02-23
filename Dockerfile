FROM python:3.10

WORKDIR /

COPY requirements.txt /

RUN pip install -U pip && pip install -r requirements.txt


COPY main.py /
COPY bd.py /


EXPOSE 5000

CMD [ "python3", "main.py" ]

