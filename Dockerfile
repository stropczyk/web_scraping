FROM python:3.7-alpine

LABEL maintainer='stropczyk'

WORKDIR /web_scraping

ENV FLASK_APP run.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "run.py" ]