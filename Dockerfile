FROM python:3.10-slim-buster

RUN mkdir -p /wgu
COPY ./api /wgu/api

RUN pip3.10 install --no-cache-dir --upgrade -r /wgu/api/requirements.txt

EXPOSE 5000

CMD ["python", "/wgu/api/app2.py"]