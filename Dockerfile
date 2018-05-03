FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    apt-utils \
    sqlite3

COPY requirments.txt /requirments.txt
RUN pip install -r requirments.txt

COPY /start-dev.sh /start-dev.sh
RUN sed -i 's/\r//' /start-dev.sh
RUN chmod +x /start-dev.sh

RUN mkdir /app
WORKDIR /app
ADD . /app/
