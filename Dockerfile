FROM python:slim

#LABEL maintainer='stropczyk'

WORKDIR /web_scraping

COPY . .

#ENV FLASK_APP run.py
#
#ENV FLASK_RUN_HOST 0.0.0.0

#RUN apk add --no-cache gcc musl-dev linux-headers

RUN python -m pip install --upgrade pip

#COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#COPY . .

EXPOSE 5000

CMD [ "python", "run.py" ]