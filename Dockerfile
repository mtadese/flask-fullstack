FROM python:3.6
LABEL maintainer="Micheal Tadese"

WORKDIR /app
ADD . /app

RUN pip3 install flask

EXPOSE 7000

CMD ["python", "demo.py"]
