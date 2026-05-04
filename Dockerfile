FROM python:3.10
COPY *.py
COPY config.json
COPY requirements.txt

CMD ["/bin/sh"]