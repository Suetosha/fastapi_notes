FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["./entrypoint.sh"]