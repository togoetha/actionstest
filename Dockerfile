FROM python:3.10
COPY main.py main.py
COPY config.json config.json
COPY requirements.txt requirements.txt

CMD ["/bin/sh"]