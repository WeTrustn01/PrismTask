FROM python:3.6-alpine

COPY . /application

WORKDIR /application

RUN python3 -m venv venv

RUN pip3 install -r requirements.txt

RUN chmod +x boot.sh

ENV FLASK_APP prism.py

EXPOSE 5000
ENTRYPOINT ["boot.sh"]
