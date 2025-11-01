
FROM fedos7777/oracle-client:latest

# ENV http_proxy=http://10.84.142.62:3128
# ENV https_proxy=http://10.84.142.62:3128
# ENV no_proxy=10.84.159.2

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app/req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY ./app .